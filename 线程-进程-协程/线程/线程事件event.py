# -*- coding:utf-8 -*-
import random
import time
from threading import Thread, Event


e = Event()


def conn():
    """测试连接"""
    count = 1
    while not e.is_set():

        print("尝试第{}次连接".format(count))
        if count > 4:
            # return TimeoutError
            raise TimeoutError
        count += 1
        e.wait(random.uniform(0.5, 2))  # 阻塞
    if e.is_set():
        # return "连接成功"
        print("连接成功")


def check_conn():
    """检查连接"""
    time.sleep(random.uniform(0.5, 2))
    e.set()  # 设置事件连接为真，表示可以连接


t1 = Thread(target=conn)
t1.start()
t2 = Thread(target=check_conn)
t2.start()
