# -*- coding:utf-8 -*-
from threading import Timer


def func():
    print("a timer")


# 定时器，第一个参数为时间（s），第二个参数为函数名
t = Timer(2, func)  # 表示两秒后执行func函数
# 定时器每隔第一个参数的时间开启一个线程
t.start()

# time.sleep() 线程内
