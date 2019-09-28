import socket

import threading

HOST = ''
PORT = 1234
ADDR = (HOST, PORT)

ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_socket.bind(ADDR)
ser_socket.listen(128)


def recv_msg(addr, cli_socket):

    while True:
        data = cli_socket.recv(1024)
        if data:
            print(f'信息来自客户端{addr}:', data.decode("utf-8"))

        else:
            print(f'客户端{addr}断开连接' + c )
            break

        send_info = input(f'服务端回复{addr}:')
        data = send_info.encode('utf-8')

        cli_socket.send(data)

    cli_socket.close()


print('等待连接...')

while True:

    cli_socket, addr = ser_socket.accept()

    recv_thread = threading.Thread(target=recv_msg, args=(addr, cli_socket),
                                   daemon=True)
    recv_thread.start()
