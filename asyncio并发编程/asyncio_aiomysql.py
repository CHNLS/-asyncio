# -*- coding:utf-8 -*-
import asyncio
import random

import aiomysql

loop = asyncio.get_event_loop()


# @asyncio.coroutine
async def test_example(name1, name2):
    # 设置charset="utf8", autocommit=True，避免数据插入不了数据库bug
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='mysql',
                                  db='async', loop=loop, charset="utf8",
                                  autocommit=True)

    cur = await conn.cursor()
    insert_sql = "insert into users (name, age) values ('{}', {}), ('{}', {})".format(name1, random.randint(18, 30), name2, random.randint(18, 30))
    await cur.execute(insert_sql)
    try:
        await cur.execute("SELECT `id`, `name`, age FROM users")
    except Exception as e:
        print(e)
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()


name1 = input("name1: ")
name2 = input("name2: ")

loop.run_until_complete(test_example(name1, name2))
