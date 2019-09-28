import socket

# import time

HOST = ''
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(ADDR)
server_sock.listen(128)

while True:
    print('等待连接...')
    conn, addr = server_sock.accept()
    print(f'连接于{addr}')

    while True:
        # 接收客户端发送的的数据总长度
        # num = conn.recv(BUFSIZ).decode("utf-8")
        # 接收数据长度以总长度计算
        data = conn.recv(1024)
        print(len(data.decode("utf-8")))
        if not data:
            break
        else:
            print('客户端信息：%s' % data.decode('utf-8'))
            # send_info = input('服务端输入>')
            # data = send_info.encode('utf-8')
            conn.send(data)

    conn.close()

server_sock.close()