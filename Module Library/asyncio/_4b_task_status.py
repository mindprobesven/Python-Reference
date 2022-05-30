#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Retrieving the status of a task coroutine
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def foo(numbers: list) -> list:
    await asyncio.sleep(5)
    return list(reversed(numbers))

async def get_task_status(coro):
    while True:
        await asyncio.sleep(1)
        print(f'Type: {type(coro)}, Name: {coro.get_name()}, Coroutine Obj: {coro.get_coro()} isDone: {coro.done()}, isCancelled: {coro.cancelled()}')
        if coro.done():
            break

async def main():
    # Create task coroutine that takes 5 seconds to be done
    task1 = asyncio.create_task(foo([1, 2, 3]), name="foo_task")
    # Create another task, passing task1, which prints that status of task1 every second until task1 is done
    task2 = asyncio.create_task(get_task_status(task1), name="get_task_status")

    result = await task1
    await task2

    print(result)

if __name__ == "__main__":
    asyncio.run(main())