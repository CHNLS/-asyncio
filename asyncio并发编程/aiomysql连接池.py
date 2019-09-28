# -*- coding:utf-8 -*-
import asyncio
import aiomysql

loop = asyncio.get_event_loop()

# @asyncio.coroutine
# def example():
#     # 设置charset="utf8", autocommit=True，避免数据插入不了数据库bug
#     pool = yield from aiomysql.create_pool(host='127.0.0.1', port=3306,
#                                       user='root', password='mysql',
#                                       db='async', loop=loop, charset="utf8",
#                                       autocommit=True)
#     with (yield from pool) as conn:
#         cur = yield from conn.cursor()
#         yield from cur.execute("SELECT 10")
#         # print(cur.description)
#         (r,) = yield from cur.fetchone()
#         assert r == 10
#
#     pool.close()
#     yield from pool.wait_closed()
#
#
# loop.run_until_complete(example())


async def example():
    # 设置charset="utf8", autocommit=True，避免数据插入不了数据库bug
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='mysql',
                                      db='async', loop=loop, charset="utf8",
                                      autocommit=True)

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT name from users;")
            print(cur.description)
            (r,) = await cur.fetchone()  # 返回元组
            res = await cur.fetchall()
            # assert r == 42
            print(r)
            print(res)

    pool.close()
    await pool.wait_closed()


loop.run_until_complete(example())
