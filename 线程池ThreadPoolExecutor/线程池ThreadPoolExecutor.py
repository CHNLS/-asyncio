# -*- coding:utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, \
    as_completed, wait, ALL_COMPLETED, FIRST_COMPLETED

"""
自动调度线程
主线程可以获取某一个线程（或者任务的）的状态，以及返回值。
当一个线程完成的时候，主线程能够立即知道。
让多线程和多进程的编码接口一致。
"""


# 参数times用来模拟网络请求的时间
def get_html(url):
    time.sleep(2)
    print("get page {} finished".format(url))
    return url


def callback(args):
    res = args.result()
    print(res)

# executor = ThreadPoolExecutor(max_workers=2)
# # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞。即合并了创建和start功能
# task1 = executor.submit(get_html, 3)
# task2 = executor.submit(get_html, 2)
# # done方法用于判定某个任务是否完成
# print(task1.done())
# # cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
# print(task2.cancel())
# time.sleep(4)
# print(task1.done())
# # result方法可以获取task的执行结果
# print(task1.result())
# executor.shutdown() 合并了close() 和 join()


# as_completed(fs, timeout=None)
# 接受2个参数，第一个是执行的线程列表
# as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务
# 先完成的任务会先通知主线程
urls = ['http://www.baidu.com', 'http://www.google.com', 'http://cn.bing.com']
executor = ThreadPoolExecutor(max_workers=3)
# all_task = [executor.submit(get_html, url) for url in urls]

# for future in as_completed(all_task):
#     data = future.result()
#     print("任务 {} 完成".format(data))


# # wait
# wait(all_task, return_when=ALL_COMPLETED)
# wait(all_task, return_when=FIRST_COMPLETED)
# print("main")


# # map 异步，不支持返回值
# for data in executor.map(get_html, urls):
#     print("任务 {} 完成".format(data))

# 回调函数 add_done_callback
with ThreadPoolExecutor(max_workers=3) as t:
    ret = t.submit(get_html, "www.xx.com")
    ret.add_done_callback(callback)


# # 使用 with 语句 ，通过 ThreadPoolExecutor 构造实例，同时传入 max_workers 参数来设置线程池中最多能同时运行的线程数目。
# with ThreadPoolExecutor(max_workers=3) as t:
#     task1 = t.submit(get_html, 3)
#     task2 = t.submit(get_html, 3)
#
#     print(task1.done())
#     print(task1.cancel())
#     time.sleep(3)
#     print(task1.done())
#     print(task2.done())
#
#     print(task1.result())
#
