import threading, queue
import ServerClientBase as SCB
import json



send_queues = {}
lock = threading.Lock()

class Server():
    HOST = '218.149.168.65' #이거 설정해두면 이 IP가진것만 클라이언트로 받을 수 있다
    PORT = 4040   #정수형으로 아무거나
    send_msg = ''
    recv_msg = ''
    clientAddr = ''
    flag_isfirst = True

    #초기화하면서 소켓하나 만들고 클라이언트 받는거 대기
    #1:1통신이라 이렇게 짰지만 다중 환경 지원하려면 다르게 짜야함
    def __init__(self):
        listen_sock = SCB.create_listen_socket(self.HOST, self.PORT)
        self.clientAddr = listen_sock.getsockname()
        print('Listening on {}'.format(clientAddr))
        self.listen_client(listen_sock)

    def listen_client(self, sock):
        client_sock, addr = sock.accept()  # 메인 쓰레드는 어셉트 상황에서 기다리고 잡히면 서브 쓰레드를 하나 만드는 것이다.
                                           # 위에서 프로그램이 대기하니까 이걸 쓰레드 처리하면 여러 클라이언트를 처리할수 있음


        # 다중클라이언트 처리할 필요가 없어서 아래부분 삭제 broadcast_msgs 함수도 삭제
        # dict타입의 queue는 thread safe가 아니다. 그래서 lock을 걸어 그 operation에 그 쓰레드만 쓰게끔 할 수 있다.
        # q = queue.Queue()
        # with lock:
        #     send_queues[client_sock.fileno()] = q

        recv_thread = threading.Thread(target=self.handle_client_recv, args=[client_sock, addr], daemon=True)
        # send_thread = threading.Thread(target=self.handle_client_send, args=[client_sock, addr], daemon=True)

        recv_thread.start()
        # send_thread.start()

    #메시지 받고 출력하는 함수
    def handle_client_recv(self, sock, addr):
        rest = bytes()
        while True:
            try:
                self.recv_msg, rest = SCB.recv_msgs(sock)
                ##################################
                #이부분 수정하면 된다
                self.recv_msg = json.loads(self.recv_msg[0])
                # print(self.recv_msg)
                #########################

            except (EOFError, ConnectionError):
                self.handle_disconnect(sock, addr)
                break

    def handle_client_send(self, sock, addr):
        try:
            SCB.send_msg(sock, self.send_msg)
            self.flag_isfirst = False
        except (ConnectionError, BrokenPipeError):
            self.handle_disconnect(sock, addr)

    def sendStatus(self, msg):
        self.send_msg = json.dumps(msg)
        self.handle_client_send(self.sock, self.clientAddr)
        self.flag_isfirst = True

    # def broadcast_msg(self, msg):
    #     with lock:
    #         for q in send_queues.values():
    #             q.put(msg)

    def handle_disconnect(self, sock, addr):
        fd = sock.fileno()
        with lock:
            q = send_queues.get(fd, None)

        if q:
            q.put(None)
            del send_queues[fd]
            addr = sock.getpeername()
            print('Client {} disconnected'.format(addr[2] + ' @ ' + addr[0]))
            sock.close()



if __name__ == '__main__':
    server = Server()
    while(1):
        x=[1,2,3]
        server.sendStatus(x)
        y = server.recv_msg
        try:
            print(y)
        except:
            pass

#쓰레드가 handle_client 함수를 자동으로 실행시킬 것이다.                             #daemon 파생된 스레드가 메인스레드와 같이 소멸할지를 결정
# thread = threading.Thread(target = handle_client, args=[client_sock, addr], daemon = True)
# thread.start()



#queue 데이터를 집어넣는 도중에 OS레벨에서 오브젝트 하나를 집었는데 끝날 때 까지
# 중간에 쓰레드가 바뀌지 않아 completely thread safe 라고 한다
#                          >>객체에 대한 연산이 atomic하다.
#하지만 GIL은 한 연산이 완료되도록 보장하지 않아 thread safe가 아니다.

#Lock