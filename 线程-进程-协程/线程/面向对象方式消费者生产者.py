import threading
import queue
import time
import random


class Producer(threading.Thread):

    def __init__(self, i, q):
        # 实例化父类方法
        super().__init__()
        self.data = q
        self.i = i
        # self.num = num

    def produce(self):
        # 循环生产
        while True:
            num = random.randint(0, 10000)
            self.data.put(num)
            # for i in range(5):
            print("生产者%d生产了%d个数据" % (self.i, num))
            time.sleep(2)

    # 重写run方法
    def run(self):
        self.produce()


class Customer(threading.Thread):

    def __init__(self, j, q):
        super().__init__()
        self.data = q
        self.j = j

    def customer(self):
        while True:
            get_num = self.data.get()
            # for j in range(5):
            print("消费者%d消费了%d个数据" % (self.j, get_num))
            time.sleep(3)

    def run(self):
        self.customer()


def main():

    q = queue.Queue()
    for i in range(5):
        p = Producer(i, q)
        p.start()

    for i in range(5):
        c = Customer(i, q)
        c.start()

    # p.join()
    # c.join()


if __name__ == '__main__':
    main()

