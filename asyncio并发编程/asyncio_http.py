# -*- coding:utf-8 -*-
import asyncio
# 建立socket连接
# reader, writer = await asyncio.open_connection(host, port)
# 写内容（发送数据）
# writer.write("xxxx".encode("utf-8"))
# 读取内容
# all_data = []
# async for line in reader:
#     data = line.decode("utf-8")
#     all_data.append(data)


# 等同于
# async def wget():
# @asyncio.coroutine，基于生成器的协程，是 async/await 语法的前身，
# 使用 yield from 语句创建的 Python 生成器，可以等待 Future 和其他协程。
# 使得旧式的基于生成器的协程能与 async/await 代码相兼容，不可用 async def 定义协程。
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()  # 由于writer中有缓冲区，如果缓冲区没满且不drain的话数据不会发送出去
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
