# 黏包现象
# 当客户端连续两次send数据 ，一次小文件会在缓冲区等待，再send一次消息会和第一次在
# 缓冲区封包一起send，会导致接收数据大于默认字节，超过部分会在下一次接收

# 解决方式：
#   将两次send消息结合算长度len()，发送给服务端确定此次接收数据的长度


import socket

HOST = 'localhost'  # 或 '127.0.0.1' ,　IPv6:HOST = '::1'
PORT = 7887
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 尝试连接服务器
client_sock.connect(ADDR)

# 一个很大的字符串
# big_str = "gas"*1000
small_str = "python"
# 通信循环
while True:
    data_info = input('输入>')
    # 计算send内容的总长度，发送给服务端
    # num = client_sock.send(str(len(big_str) + len(data_info)).encode("utf-8"))
    # num = client_sock.send(str(len(small_str) + len(data_info)).encode("utf-8"))

    # 为防止黏包现象，加一个recv()阻塞
    # client_sock.recv(1024)
    data = data_info.encode('utf-8')
    if not data:
        break
    client_sock.send(data)
    # client_sock.send(big_str.encode("utf-8"))
    client_sock.send(small_str.encode("utf-8"))
    data = client_sock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

client_sock.close()
