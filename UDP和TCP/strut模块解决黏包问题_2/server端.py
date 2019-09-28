import socket

import struct

# import time

HOST = ''
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ser_sock.bind(ADDR)
tcp_ser_sock.listen(128)

while True:
    print('等待连接...')
    tcp_cli_sock, addr = tcp_ser_sock.accept()
    print(f'连接于{addr}')

    while True:
        # 接收客户端发送的的数据长度的bytes类
        num_recv = tcp_cli_sock.recv(4)  # 只有4个字节

        # 将接收的num_recv转换为元组，取索引0的元素
        num = struct.unpack("i", num_recv)[0]

        # 接收数据长度以总长度计算
        data = tcp_cli_sock.recv(num)
        print(len(data.decode("utf-8")))
        if not data:
            break
        else:
            print('客户端信息：%s' % data.decode('utf-8'))
            send_info = input('服务端输入>')
            data = send_info.encode('utf-8')
            tcp_cli_sock.send(data)

    tcp_cli_sock.close()

tcp_ser_sock.close()