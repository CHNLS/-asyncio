import greenlet
import time


def func1():
    for i in range(5):
        print(f'第{i+1}次：这是func1')
        i += 1
        time.sleep(0.2)
        # 切换到func2
        gl2.switch()


def func2():
    for i in range(5):
        print(f'第{i+1}次：这是func2')
        i += 1
        time.sleep(0.2)
        # 切换到func1
        gl1.switch()


if __name__ == '__main__':

    # 创建协程指定的任务
    gl1 = greenlet.greenlet(func1)
    gl2 = greenlet.greenlet(func2)

    # 切换到第一个任务
    gl1.switch()

