# -*- coding:utf-8 -*-
import asyncio


# Python3.7
import platform


async def nested():
    return 42


python_version = platform.python_version().rpartition(".")[0]


async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    # task = asyncio.create_task(nested())

    if float(python_version) >= 3.7:
        print("3.7版本")
        task = asyncio.create_task(nested())
    else:
        print("3.7以下版本")
        task = asyncio.ensure_future(nested())
    print(task)

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    # await task


if float(python_version) >= 3.7:
    asyncio.run(main())
else:
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main())
    loop.run_until_complete(task)
