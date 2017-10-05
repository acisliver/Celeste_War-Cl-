import socket

HOST = '127.0.0.1' #바꿔야할부분
PORT = 4040
conn = None

#데이타 배열에서 메시지 하나와 나머지부분을 골라낸다.
def parse_recvd_data(data):
    parts = data.split(b'\0')
    msgs = parts[:-1]
    rest = parts[-1]
    return [msgs, rest]

#서버측 소켓을 어셉트단계까지 만든다.
def create_listen_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((host,port))
    sock.listen(100)
    # conn, addr = socke.accept()
    return sock

#persistent connection 접근법이 가진 문제 해결
#메세지들은 Null값을 통해 구분이 되어진다.
#메시지들은 끊어질 수 있기 때문에 null값으로만 구분이 되어야 한다.
def recv_msgs(sock, data = bytes()):
    msgs = []
    while not msgs:
        recvd = sock.recv(4096)
        if not recvd:
            raise ConnectionError()
        data =  data + recvd
        # if b'\0' in recvd:
        #     msg = data.rstrip(b'\0')
        (msgs, rest) = parse_recvd_data(data)
    msgs = [msg.decode('utf-8') for msg in msgs]
    return (msgs, rest)


def prep_msg(msg):
    msg += '\0'
    return msg.encode('utf-8')

def send_msg(sock, msg):
    """ Send a string over a socket, preparing it first """
    data = prep_msg(msg)
    sock.sendall(data)

if __name__ == '__main__':
    create_listen_socket(HOST, 4040)
