# -*- coding:utf-8 -*-
import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine


metadata = sa.MetaData()

tbl = sa.Table('person', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('name', sa.String(255)),
               # sa.Column("age", sa.Integer)
               )


async def go(loop):
    engine = await create_engine(user='root', db='async_sql_test',
                                 host='127.0.0.1', password='mysql', loop=loop)
    async with engine.acquire() as conn:
        await conn.execute(tbl.insert().values(name='abc'))
        await conn.execute(tbl.insert().values(name='xyz'))

        async for row in conn.execute(tbl.select()):
            # print(row)
            print(row.id, row.name)

    engine.close()
    await engine.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
