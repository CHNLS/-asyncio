import socket
import struct

HOST = 'localhost'  # 或 '127.0.0.1' ,　IPv6:HOST = '::1'
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_sock.setblocking(False)  
# 为False时，connect则不会阻塞，但需要确定服务已经连接上，不停询问连接状态
# 尝试连接服务器，阻塞，连接不上一直等待，如果设置不等待，可在连接前设置
client_sock.connect(ADDR)

# big_str = "gas"*1000
# small_str = "python"

# 通信循环
while True:
    data_info = input('输入>')
    if not data_info:
        break
    # data = data_info.encode('utf-8')
    client_sock.send(data_info.encode("utf-8"))
    # client_sock.send(big_str.encode("utf-8"))
    # client_sock.send(small_str.encode("utf-8"))
    data_recv = client_sock.recv(BUFSIZ)
    if not data_recv:
        break
    print(data_recv.decode('utf-8'))

client_sock.close()