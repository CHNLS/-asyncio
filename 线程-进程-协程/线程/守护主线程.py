import threading

import time


def a():

    # 获取当前子线程
    current_thread = threading.current_thread()
    print(current_thread)
    for i in range(5):
        print('这是子线程')
        time.sleep(0.1)


def main():
    time.sleep(0.3)
    print('这是主线程')


# 设置守护主线程:主线程执行完毕,子线程直接退出销毁
a_thread = threading.Thread(target=a, daemon=True)
a_thread.start()

# 主线程会在所有子线程结束后再结束
main()

# # 获取活动线程数的列表
# thread_list = threading.enumerate()
# print(thread_list)
#
# # 子线程执行完自动销毁
# time.sleep(1)
# thread_list = threading.enumerate()
# print(thread_list)
