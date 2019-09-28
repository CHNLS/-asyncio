from multiprocessing import Queue

# 创建队列，队列消息为5个
queue = Queue(5)
# 向队列放数据
queue.put(1)
queue.put('a')
queue.put((1, 2))
queue.put([4, 5])
queue.put({'a': 1})

# 不能一次性添加多个数据
# queue.put(1, 'a', (1, 2), [4, 5], {'a': 1})

# 当队列消息已放满，再put()数据会等待
# queue.put(2323)
# 使用put_nowait()不等待，直接报错
# queue.put_nowait(2323)

# 查看队列是否满了
print('满了没？', queue.full())

# 查看队列消息个数
print('个数:', queue.qsize())

# 获取队列消息
value = queue.get()
value = queue.get()
print(value)

# 当队列消息get完后再次使用get会等待
value = queue.get()
value = queue.get()
value = queue.get()

# 再次执行一下代码会等待，只有队列put值后才会取
# 使用get_nowait()不等待，直接报错，不建议使用
# value = queue.get()
# value = queue.get_nowait()
print('值：', value)

# 查看队列是否空了
print('空了没？', queue.empty())