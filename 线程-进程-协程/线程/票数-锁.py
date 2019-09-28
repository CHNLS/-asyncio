import threading
import time

g_ticket = 100
i = 0

lock = threading.Lock()


def sold(n):

    global g_ticket, i
    while True:
        # 上锁
        lock.acquire()
        if g_ticket:
            i += 1
            g_ticket -= 1
            time.sleep(0.1)
            print('线程%d第%d张，剩%d张' % (n, i, g_ticket))
            # 解锁，让其他线程抢锁
            lock.release()

        else:
            # 解锁
            lock.release()
            break


for index in range(6):
    sold_thread = threading.Thread(target=sold, args=(index+1, ))

    sold_thread.start()