import threading
import queue
import time
import random


def producer(i, q):
    while True:
        num = random.randint(0, 10000)
        q.put(num)
        print("生产者%d生产了%d个数据" % (i, num))
        time.sleep(1)
    # q.task_done()


def customer(j, q):
    while True:
        num_get = q.get()
        if not num_get:
            break
        print("消费者%d消费了%d个数据" % (j, num_get))
        time.sleep(3)
    # q.task_done()


if __name__ == '__main__':
    q = queue.Queue()
    # 启动生产者
    for i in range(3):
        p = threading.Thread(target=producer, args=(i, q))
        p.start()
    # 启动消费者
    for i in range(4):
        c = threading.Thread(target=customer, args=(i, q))
        c.start()
