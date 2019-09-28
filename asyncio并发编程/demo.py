# -*- coding:utf-8 -*-
import asyncio
import time


async def get_html(url):
    print("start")
    # 此处不能使用time.sleep()，time.sleep()为同步阻塞，耗时操作在高并发中会增加请求时间
    # 可使用任务列表测试时间
    # time.sleep(2)  # 时长20s
    await asyncio.sleep(2)  # 时长2s
    print("end")


if __name__ == '__main__':
    s = time.time()
    # 获取事件循环对象
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("www.baidu.com"))

    # 任务列表，可等待对象
    # 等待对象有三种主要类型: 协程, 任务和Future.一个对象可以在 await 语句中使用，那么它就是可等待对象
    tasks = [get_html("www.baidu.com") for i in range(10)]
    # Python3.7中使用create_task创建多个协程
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - s)
