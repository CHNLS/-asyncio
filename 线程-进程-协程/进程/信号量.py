import multiprocessing
import time
import random

from atexit import register
from threading import BoundedSemaphore


def semaphore(i, sem):
    sem.acquire()
    print("%d执行了" % i)
    time.sleep(random.randint(2, 5))
    print("%d执行完了" % i)
    sem.release()


if __name__ == '__main__':

    # 信号量，每次只能有4个进程执行
    sem = multiprocessing.Semaphore(4)
    for i in range(20):
        p = multiprocessing.Process(target=semaphore, args=(i, sem))
        p.start()