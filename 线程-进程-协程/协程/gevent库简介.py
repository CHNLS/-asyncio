import gevent


def func(n):
    for i in range(4):
        print(gevent.getcurrent(), '第%d次，执行' % i)
        i += 1
        # # 用来模拟一个耗时操作，注意不是time模块中的sleep
        # # 没有gevent的sleep耗时，每个协程会一次执行
        # # 有耗时，则会依次每个协程执行一次再次循环
        gevent.sleep(1)


g1 = gevent.spawn(func, 3)
g2 = gevent.spawn(func, 3)
g3 = gevent.spawn(func, 3)

g1.join()
g2.join()
g3.join()
