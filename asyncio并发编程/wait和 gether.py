# -*- coding:utf-8 -*-
import asyncio
import threading
import time


async def get_html(url):  # 定义协程函数
    print("start---{}".format(threading.current_thread()))
    await asyncio.sleep(2)  # 时长2s
    print("end---{}".format(threading.current_thread()))
    return url  # 返回对象为协程对象


# python3.7 语法
async def main():
    tasks1 = [get_html("www.taobao.com") for i in range(3)]
    tasks2 = [get_html("www.tianmao.com") for i in range(3)]
    await asyncio.gather(*tasks1, *tasks2)

if __name__ == '__main__':
    start = time.time()

    # wait
    # tasks = [get_html("www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # gather
    # 可以将任务分组
    # tasks1 = [get_html("www.taobao.com") for i in range(3)]
    # tasks2 = [get_html("www.tianmao.com") for i in range(3)]
    # # loop.run_until_complete(asyncio.gather(*tasks1, *tasks2))
    # # 或者
    # group1 = asyncio.gather(*tasks1)
    # group2 = asyncio.gather(*tasks2)
    # # group2.cancel()  # 取消分组
    # loop.run_until_complete(asyncio.gather(group1, group2))

    # python3.7 语法
    asyncio.run(main())
    print(time.time() - start)
