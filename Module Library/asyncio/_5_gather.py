#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Gather - Running tasks concurrently
#
# Run awaitable objects in the aws sequence concurrently.
#
# If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of 
# result values corresponds to the order of awaitables in aws.
#
# If return_exceptions is False (default), the first raised exception is immediately propagated to the task that 
# awaits on gather(). Other awaitables in the aws sequence won’t be cancelled and will continue to run.
#
# If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result 
# list.
#
# If gather() is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.
#
# If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import random

async def request_db_data() -> int:
    # Fake database call taking one second
    await asyncio.sleep(1)
    return random.randrange(1, 10)

async def get_all_tasks_status():
    await asyncio.sleep(0)
    print(list(task.get_name() for task in asyncio.all_tasks()))    # ['Task-1', 'Task1', 'Task2', 'Task-4']
    return 'Done'

async def main():
    task1 = asyncio.create_task(request_db_data(), name='Task1')
    task2 = asyncio.create_task(request_db_data(), name='Task2')

    results = await asyncio.gather(
        # These tasks were created manually using create_task()
        task1, 
        task2, 
        # If any awaitable in aws is a coroutine like get_all_tasks_status(), it is automatically scheduled as a Task.
        get_all_tasks_status())
    
    # If all awaitables are completed successfully, the result is an aggregate list of returned values.
    print(results)  # [8, 4, 'Done']

if __name__ == "__main__":
    asyncio.run(main())