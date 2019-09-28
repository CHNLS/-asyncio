# -*- coding:utf-8 -*-
import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def get_html(url):
    print("start---{}".format(threading.current_thread()))
    # await asyncio.sleep(2)  # 时长2s
    print("end---{}".format(threading.current_thread()))
    return url


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(5)
    tasks = []
    for i in range(8):
        url = "http://www.test.com/{}".format(i)
        task = loop.run_in_executor(executor, get_html, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)

