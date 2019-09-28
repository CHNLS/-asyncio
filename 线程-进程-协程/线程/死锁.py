import threading

# import time

# 创建锁
lock = threading.Lock()


def func(index):

    # 上锁
    lock.acquire()

    my_list = [3, 6, 8, 1]
    # 判断下标释放越界
    if index >= len(my_list):
        print('越界下标', index)
        # 当索引超过列表长度时，需要进行解锁，如果不进行解锁，则会造成死锁(程序未停止)
        lock.release()
        return

    value = my_list[index]
    print(value)
    # 解锁
    lock.release()


for i in range(30):
    func_thread = threading.Thread(target=func, args=(i, ))
    func_thread.start()