import socket
import threading

import ServerClientBase as SCB


class Client():
    HOST = '127.0.0.1'
    PORT = SCB.PORT
    send_msg = ''
    recv_msg = ''
    sock = None
    flag_isfirst = True

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))
        # 반드시 스레드를 통해서 실행시킬것
        thread_send = threading.Thread(target=self.handle_input, args=[self.sock], daemon=True)
        thread_send.start()

    def handle_input(self, sock):
        while True:
            if self.flag_isfirst:
                try:
                    SCB.send_msg(sock, self.send_msg)
                    self.flag_isfirst = False
                except ConnectionError:
                    print('Socket error')
                    break

    def recv_msgs(self, data=bytes()):
        recvd = self.sock.recv(4096)
        if not recvd:
            raise ConnectionError()
        data = data + recvd
        (self.recv_msg, rest) = SCB.parse_recvd_data(data)
        self.recv_msg = [msg.decode('utf-8') for msg in self.recv_msg]
        return self.recv_msg

    def sendstate(self, sendlist):
        self.send_msg = sendlist
        self.flag_isfirst = True

if '__main__' == __name__:
    client = Client()
    while(1):
        x = input()
        client.sendstate(x)
        y = client.recv_msgs()
        print(y)