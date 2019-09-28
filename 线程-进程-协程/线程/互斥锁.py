import threading

g_num = 0
# 创建锁
lock = threading.Lock()


def sum1():
    # 上锁,锁定线程sum1
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print(g_num)
    # 解锁
    lock.release()

# 每次只有一个线程可以获得锁，如果另一个线程试图获得锁，那个会变为“blocked”状态，即“阻塞”
# 知道拥有锁的线程使用release释放锁，锁进入“unlocked”状态，另一个线程才能获得锁


sum2 = sum1
print(sum1)
print(sum2)


# def sum3():
#     for i in range(1000000):
#         global g_num
#         g_num += 1
#     print(g_num)
#
# print(sum3)

sum1_thread = threading.Thread(target=sum1)
sum2_thread = threading.Thread(target=sum2)
# sum3_thread = threading.Thread(target=sum3)

sum1_thread.start()
# # 线程等待(同步)，必须等待第一个线程执行完，再执行下一个线程
# # 如果不执行等待，线程同时进行，会导致同一数据处理
# sum1_thread.join()

sum2_thread.start()
# sum2_thread.join()
#
# sum3_thread.start()
