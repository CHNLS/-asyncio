import asyncio


async def get_html(url):
    print("start")
    await asyncio.sleep(2)  # 时长2s
    print("end")
    return url


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_html("www.baidu.com"))
    loop.run_until_complete(future)
    res = future.result()  # 获取返回值
    # 或者
    # task = loop.create_task(get_html("www.baidu.com"))
    # loop.run_until_complete(task)
    # res = task.result()
    print(res)
