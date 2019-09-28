
import threading

import time

loops = [4, 2]


class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.func = func
        self.args = args
        self.name = name

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


def loop(nloop, nsec):
    print('开始>', nloop, ':', time.ctime())
    time.sleep(nsec)
    print('结束>', nloop, ':', time.ctime())


def main():
    print('开始main>', time.ctime())
    threads = []
    nloops = list(range(len(loops)))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i],), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('完', time.ctime())


if __name__ == '__main__':
    main()
