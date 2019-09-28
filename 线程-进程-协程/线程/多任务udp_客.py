import socket

import threading

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)

lock = threading.Lock()


def send(cli_soc):

    lock.acquire()

    while True:

        send_msg = input('输入信息>')
        data = send_msg.encode('utf-8')

        cli_soc.sendto(data, ADDR)

        lock.release()
        return


def receive(cli_soc):

    lock.acquire()
    while True:
        data, addr = cli_soc.recvfrom(1024)
        print('服务端信息:%s' % data.decode('utf-8'))

        lock.release()
        return


if __name__ == '__main__':

    cli_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cli_send_thread = threading.Thread(target=send, args=(cli_soc,))
    cli_rec_thread = threading.Thread(target=receive, args=(cli_soc,))

    cli_send_thread.start()
    # cli_send_thread.join()

    receive(cli_soc)
    # cli_rec_thread.start()
    # cli_rec_thread.join()

    cli_soc.close()


