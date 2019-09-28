import threading

import time

import os


def a(msg):
    for i in range(3):
        # os.getpid() 获取当前进程id号(可在任务管理器查看)
        print('%s: %s' % (msg, os.getpid()))
        time.sleep(0.1)


def b(msg):
    for i in range(3):
        print('%s--%s' % (msg, os.getpid()))
        time.sleep(0.1)


def c():
    for i in range(3):
        print('c线程--%s' % os.getpid())
        time.sleep(0.1)


def main():
    print('主线程> %s' % os.getpid())

    a_thread = threading.Thread(target=a, args=('a线程',))
    b_thread = threading.Thread(target=b, kwargs={'msg': 'b线程'})
    # c_thread = threading.Thread(target=c)

    a_thread.start()
    b_thread.start()
    # c_thread.start()

    c()


if __name__ == '__main__':
    main()