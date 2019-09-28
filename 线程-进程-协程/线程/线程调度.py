import threading
import time

condition = threading.Condition()
# condition中 acquire锁为递归锁，不会造成死锁


def func1():
    with condition:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 线程等待，func2执行
            condition.wait()
            condition.notify()  # 传递信号，只能为整数，表示放行几个信号
            # condition.notify() # 全部


def func2():
    with condition:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 线程执行
            condition.notify()
            # 执行完等待
            condition.wait()


threading.Thread(target=func1).start()
threading.Thread(target=func2).start()