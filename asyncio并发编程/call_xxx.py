# -*- coding:utf-8 -*-
# call_soon_threadsafe
import asyncio


# def callback(times):
#     print(f"sleep {times} times")
def callback(times, loop):
    print(f"{loop.time()} times")


def stop_loop(loop):
    loop.stop()


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.call_soon(callback, 2)
#     # loop.stop()
#     loop.call_soon(stop_loop, loop)
#     loop.run_forever()  # 不可少


# loop.call_later(delay, callback, *args, context=None)
# 延时调用，即在给定的delay时间后调用callback
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.call_later(2, callback, 2)
#     loop.call_later(1, callback, 1)
#     loop.call_later(3, callback, 3)  # 按延时时间大小顺序
#     loop.call_soon(callback, 4)  # 结果call_soon 比call_later 要快
#     # loop.stop()
#     # loop.call_soon(stop_loop, loop)
#     loop.run_forever()


# loop.call_at(when, callback, *args, context=None)
# 行为与 call_later() 相同
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, callback, 2, loop)
    loop.call_at(now+1, callback, 1, loop)
    loop.call_at(now+3, callback, 3, loop)  
    loop.call_soon(callback, 4, loop)  # 结果和call_later 一样
    # loop.stop()
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()

