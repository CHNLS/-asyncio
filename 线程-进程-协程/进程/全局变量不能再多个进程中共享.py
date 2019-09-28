import multiprocessing

g_sum = 0


def sum1():
    for i in range(1000000):
        global g_sum
        g_sum += 1
    print(g_sum)


sum2 = sum1

if __name__ == '__main__':

    print(g_sum)

    sum1_process = multiprocessing.Process(target=sum1)
    sum2_process = multiprocessing.Process(target=sum2)

    sum1_process.start()
    sum1_process.join()

    sum2_process.start()
    sum2_process.join()

    print('over')