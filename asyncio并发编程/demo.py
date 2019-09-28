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
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("www.baidu.com"))

    # 任务列表
    tasks = [get_html("www.baidu.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - s)
