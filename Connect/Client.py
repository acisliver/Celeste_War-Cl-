import socket
import threading
import json
import ServerClientBase as SCB


class Client():
    HOST = '218.149.168.37'
    PORT = SCB.PORT
    send_msg = ''
    recv_msg = ''
    sock = None
    flag_isfirst = False

    def __init__(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        # 반드시 스레드를 통해서 실행시킬것
        # thread_send = threading.Thread(target=self.handle_input, args=[self.sock], daemon = True)
        thread_recv = threading.Thread(target=self.recv_msgs, args = [bytes()], daemon = True)
        # thread_send.start()
        thread_recv.start()

    def handle_input(self, sock):
        # while True:
        #     # print(threading.active_count())
        #     if self.flag_isfirst:
        try:
            SCB.send_msg(sock, self.send_msg)
            # self.flag_isfirst = False
        except ConnectionError:
            print('Socket error')
                    # break


    def recv_msgs(self, data=bytes()):
        while(1):
            recvd = self.sock.recv(4096)

            if not recvd:
                raise ConnectionError()
            data = data + recvd
            # print(recvd)
            xxx = recvd
            (xxx, rest) = SCB.parse_recvd_data(data)
            # print(xxx)
            xxx = [msg.decode('utf-8') for msg in xxx]

            # self.recv_msg = recvd
            # (self.recv_msg, rest) = SCB.parse_recvd_data(data)
            # self.recv_msg = [msg.decode('utf-8') for msg in self.recv_msg]
            string = ''
            for x in xxx :
                string += x
            try:
                self.recv_msg = json.loads(string)
            except:
                pass
        return self.recv_msg

    def sendstate(self, sendlist):
        self.send_msg = json.dumps(sendlist)
        self.handle_input(self.sock)
        self.flag_isfirst = True

if '__main__' == __name__:
    client = Client()
    while(1):
        x=[4,5,6]
        client.sendstate(x)
        youuse = client.recv_msg
        print(youuse)
