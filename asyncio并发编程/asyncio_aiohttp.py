import asyncio
from pprint import pprint

from aiohttp import ClientSession


async def hello():
    async with ClientSession() as session:
        async with session.get("https://www.sina.com.cn") as response:
            resp = await response.read()
            # print(resp)
            pprint(resp)


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
