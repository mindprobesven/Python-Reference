#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# as_completed()
#
# Run awaitable objects in the aws iterable concurrently. Return an iterator of coroutines. Each coroutine returned 
# can be awaited to get the earliest next result from the iterable of the remaining awaitables.
#
# Raises asyncio.TimeoutError if the timeout occurs before all Futures are done.
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def get_request_slow():
    await asyncio.sleep(3)
    return 'slow'

async def get_request_fast():
    await asyncio.sleep(1)
    return 'fast'
  
async def main():
    # This task requires 3 seconds to be done
    task_slow = asyncio.create_task(get_request_slow(), name='Task Slow')
    # This task requires only 1 second to be done. It's faster.
    task_fast = asyncio.create_task(get_request_fast(), name='Task Fast')

    # as_completed() returns an iterator of coroutines.
    # Each coroutine returned can be awaited to get the earliest next result from the iterable of the remaining 
    # awaitables.
    for coro in asyncio.as_completed((task_slow, task_fast), timeout=5.0):
        next_earliest_result = await coro
        print(next_earliest_result)     # fast, slow

if __name__ == "__main__":
    asyncio.run(main())