#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Awaitables
#
# An object is an awaitable object if it can be used in an await expression. There are three main types of 
# awaitable objects: coroutines, Tasks, and Futures.
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def nested():
    return 42

async def main():
    # 1. Python coroutines are awaitables and therefore can be awaited from other coroutines
    print (await nested())

    # 2. Tasks are awaitables and are used to schedule coroutines concurrently.
    task1 = asyncio.create_task(nested())
    print(await task1)

    # 3. Future. Run awaitable objects in the sequence concurrently. If all awaitables are completed successfully, 
    # the result is an aggregate list of returned values.
    task2 = asyncio.create_task(nested())
    task3 = asyncio.create_task(nested())
    task2_result, taks3_result = await asyncio.gather(task2, task3)
    print(task2_result)
    print(taks3_result)

if __name__ == "__main__":
    asyncio.run(main())