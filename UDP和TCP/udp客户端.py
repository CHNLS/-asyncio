import socket

HOST = 'localhost'  # 或 '127.0.0.1' ,　IPv6:HOST = '::1'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 通信循环
while True:
    data_info = input('输入>')
    data = data_info.encode('utf-8')
    if not data:
        break
    client_sock.sendto(data, ADDR)
    data, addr = client_sock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

client_sock.close()
