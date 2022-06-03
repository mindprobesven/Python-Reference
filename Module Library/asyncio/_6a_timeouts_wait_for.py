#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Timeouts - wait_for()
#
# Wait for the aw awaitable to complete with a timeout.
#
# If aw is a coroutine it is automatically scheduled as a Task.
# 
# timeout can either be None or a float or int number of seconds to wait for. If timeout is None, block until the 
# future completes.
# 
# If a timeout occurs, it cancels the task and raises asyncio.TimeoutError.
#
# To avoid the task cancellation, wrap it in shield().
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def get_all_tasks_status():
    await asyncio.sleep(0)
    print(list(task.get_name() for task in asyncio.all_tasks()))
    return 'Done'
  
async def main():
    task1 = asyncio.create_task(get_all_tasks_status(), name='get_all_tasks_status_task')
    # This will wait for the awaitable coroutine with a timeout. This coroutine is automatically scheduled as a Task.
    # If a timeout occurs, it cancels the task and raises asyncio.TimeoutError.
    task2 = asyncio.wait_for(eternity(), timeout=1.0)

    try:
        results = await asyncio.gather(task1, task2)
        print(results)
    except asyncio.TimeoutError:
        print('timeout!')

if __name__ == "__main__":
    asyncio.run(main())