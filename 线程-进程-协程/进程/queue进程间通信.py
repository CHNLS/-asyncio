import multiprocessing

import time


def add(queue):

    for i in range(10):
        if queue.full():
            print('满了')
            break
        queue.put(i)
        print(i)
        time.sleep(0.1)


def read(queue):
    while True:
        if queue.empty():
            print('空了')
            break
        value = queue.get()
        print(value)
        time.sleep(0.1)


if __name__ == '__main__':

    queue = multiprocessing.Queue(5)

    add_process = multiprocessing.Process(target=add, args=(queue,))
    read_process = multiprocessing.Process(target=read, args=(queue,))

    add_process.start()
    add_process.join()

    read_process.start()
