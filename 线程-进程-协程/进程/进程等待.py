import multiprocessing

import os

import time


def run(str):
    for i in range(5):
        # os.getpid() 获取当前进程id号(可在任务管理器查看)
        # os.getppid() 获得主(父)进程号
        print('哈哈,%s %s--%s ' % (str, os.getpid(), os.getppid()))
        print(time.ctime())


if __name__ == '__main__':

    print('\n主>%s' % os.getpid())

    r = multiprocessing.Process(target=run, args=('你哈毛！',))
    r.start()
    # 进程等待，当次进程执行完毕，在执行主进程(同线程)
    r.join()

    print(time.ctime(), '\n')