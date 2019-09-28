import socket
import struct

# import time

HOST = ''
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(ADDR)
server_sock.listen(128)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
# 		sock.bind()

while True:
    print('等待连接...')
    conn, addr = server_sock.accept()
    print(f'连接于{addr}')

    while True:
        data = conn.recv(BUFSIZ)
        if not data:
            break
        else:
            print('客户端信息：%s' % data.decode('utf-8'))
            send_info = input('服务端输入>')
            data = send_info.encode('utf-8')
            conn.send(data)

    conn.close()

server_sock.close()
