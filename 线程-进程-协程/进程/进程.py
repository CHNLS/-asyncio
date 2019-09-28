import multiprocessing

import os

import time


def run(str):
    for i in range(5):
        # os.getpid() 获取当前进程id号(可在任务管理器查看,需死循环)
        # os.getppid() 获得主(父)进程号
        print('哈哈,%s %s--%s ' % (str, os.getpid(), os.getppid()))
        print(time.ctime())


if __name__ == '__main__':
    print('主>%s' % os.getpid())
    print(time.ctime())

    r = multiprocessing.Process(target=run, args=('你哈毛！',))
    r.start()