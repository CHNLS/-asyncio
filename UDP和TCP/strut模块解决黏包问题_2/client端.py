
import socket

import struct

HOST = 'localhost'  # 或 '127.0.0.1' ,　IPv6:HOST = '::1'
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接
tcp_cli_sock.connect(ADDR)

# 一个很大的字符串
big_str = "gas"*1000

# 通信循环
while True:
    data_info = input('输入>')
    # 计算send内容的总长度，发送给服务端
    len_num = len(big_str) + len(data_info)

    # 将要发送的字符串长度转换,为bytes类
    num = struct.pack("i", len_num)
    # 将长度发送
    tcp_cli_sock.send(num)

    data = data_info.encode('utf-8')
    if not data:
        break
    tcp_cli_sock.send(data)
    tcp_cli_sock.send(big_str.encode("utf-8"))

    data = tcp_cli_sock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcp_cli_sock.close()
