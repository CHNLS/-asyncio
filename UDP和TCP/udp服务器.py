import socket


# import time

HOST = ''
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字与地址绑定
server_sock.bind(ADDR)

# 服务器无线循环
while True:
    print('等待信息...')

    data_info, addr = server_sock.recvfrom(BUFSIZ)
    data = data_info.decode('utf-8')
    print(f'信息来自{addr}:{data}')
    msg = input('服务端输入>')
    server_sock.sendto(bytes(f'{msg}', encoding='utf-8'), addr)

# 关闭服务器套接字
server_sock.close()
