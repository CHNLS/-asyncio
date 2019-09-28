import socket

import threading

import time


HOST = ''
PORT = 12345
ADDR = (HOST, PORT)

lock = threading.Lock()


def rec(ser_soc):

    lock.acquire()

    print('等待信息...')
    while True:

        data_info, addr = ser_soc.recvfrom(1024)
        data = data_info.decode('utf-8')
        print(f'信息来自{addr}：{data}')

        lock.release()
        return


def send(ser_soc):

    time.sleep(0.1)

    lock.acquire()

    while True:
        msg = input('服务端输入>')
        ser_soc.sendto(bytes(f'{msg}', encoding='utf-8'), ADDR)

        lock.release()
        return


if __name__ == '__main__':

    ser_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ser_soc.bind(ADDR)
    # 创建receive线程
    ser_rec_thread = threading.Thread(target=rec, args=(ser_soc,))

    ser_rec_thread.start()
    # 线程等待
    # ser_rec_thread.join()

    send(ser_soc)

    ser_soc.close()