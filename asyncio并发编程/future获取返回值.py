# -*- coding:utf-8 -*-
import asyncio
import platform
import selectors
import sys
import threading


async def get_html(url):
    print("start---{}".format(threading.current_thread()))
    await asyncio.sleep(2)  # 时长2s
    print("end---{}".format(threading.current_thread()))
    return url


if __name__ == '__main__':
    # selector = selectors.SelectSelector()

    # 关于selectors
    # def accept(sock, mask):
    #     pass
    #     # 注册conn，回调 read函数
    #     sel.register(conn, selectors.EVENT_READ, read)
    # 注册server事件：
    # 参数一：sock 进行监听
    # 参数二：selectors.EVENT_READ 执行动作
    # 参数三：accept,只要来一个链接就回调这个函数
    # sel.register(sock, selectors.EVENT_READ, accept)

    # loop = asyncio.SelectorEventLoop(selector)
    # asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    # 创建future对象，和asyncio中future对象不一样，此对象不可等待
    # loop_future = loop.create_future()
    # loop_data = loop.create_task(get_html("www.baidu.com"))
    # loop.run_until_complete(loop_data)
    # print(loop_data.result())

    # Future是一种特殊的低层级可等待对象，表示一个异步操作的最终结果。
    # 当一个Future对象被等待，这意味着协程将保持等待直到该Future对象在其他地方操作完毕。
    # 在asyncio中需要Future对象以便允许通过 async / await 使用基于回调的代码。
    # 通常情况下没有必要在应用层级的代码中创建Future对象。
    # Future对象有时会由库和某些asyncioAPI暴露给用户，用作可等待对象

    # 使用与所有Python版本
    task = asyncio.ensure_future(get_html("www.baidu.com"))
    # print(sys.version.split(" ")[0].rpartition(".")[0])
    # print(sys.version_info)

    # python_version = platform.python_version().rpartition(".")[0]
    # if float(python_version) >= 3.7:
    #     task = asyncio.create_task(get_html("www.baidu.com"))
    # else:
    #     task = asyncio.ensure_future(get_html("www.baidu.com"))
    loop.run_until_complete(task)
    res = task.result()  # 获取返回值
    # 或者
    # task = loop.create_task(get_html("www.baidu.com"))
    # loop.run_until_complete(task)
    # res = task.result()
    print(res)
