# -*- coding:utf-8 -*-
# 提示：终端运行
import asyncio
import time


async def get_html(url):
    print("start")
    await asyncio.sleep(2)  # 时长2s
    print("end")
    return url


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()

    tasks1 = [get_html("www.taobao.com") for i in range(3)]
    tasks2 = [get_html("www.tianmao.com") for i in range(3)]
    # loop.run_until_complete(asyncio.gather(*tasks1, *tasks2))
    # 或者
    group1 = asyncio.gather(*tasks1)
    group2 = asyncio.gather(*tasks2)
    try:
        loop.run_until_complete(asyncio.gather(group1, group2))
    except KeyboardInterrupt as e:  # ctrl + c 取消
        all_tasks = asyncio.Task.all_tasks()  # 获取所有任务
        # print(all_tasks)
        for task in all_tasks:
            task.cancel()  # 返回值为True 或 False
            print("cancel task")
        loop.stop()  # 停止事件循环
        loop.run_forever()  # 此步骤一定要有，不然报错
    finally:
        loop.close()

    print(time.time() - start)

