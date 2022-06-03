#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Timeouts - wait()
#
# Run awaitable objects in the aws iterable concurrently and block until the condition specified by return_when.
# timeout (a float or int), if specified, can be used to control the maximum number of seconds to wait before 
# returning.
#
# Note that this function does not raise asyncio.TimeoutError. Futures or Tasks that aren’t done when the timeout 
# occurs are simply returned in the second set.
#
# return_when indicates when this function should return. It must be one of the following constants: FIRST_COMPLETED,
# FIRST_EXCEPTION, ALL_COMPLETED
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def get_request_slow():
    await asyncio.sleep(10)
    print('Request slow done')

async def get_request_fast():
    await asyncio.sleep(2)
    print('Request fast done')
  
async def main():
    # This task requires 10 seconds to be done
    task_slow = asyncio.create_task(get_request_slow(), name='Task Slow')
    # This task requires only 2 seconds to be done. It´s faster.
    task_fast = asyncio.create_task(get_request_fast(), name='Task Fast')

    # Here we use wait(), which returns two sets of Tasks/Futures: (done, pending)
    # The return_when indicates when the wait() function should return.
    # In this example, the task that completes first within the timeout will be in the "done" set.
    # The tasks that are still pending will be in the "pending" set.
    done, pending = await asyncio.wait({task_slow, task_fast}, timeout=5.0, return_when='FIRST_COMPLETED')

    print(done)
    print(pending)

if __name__ == "__main__":
    asyncio.run(main())