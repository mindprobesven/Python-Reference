#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Creating Tasks
#
# Wrap the coroutine into a Task and schedule its execution. Return the Task object.
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def foo(numbers: list) -> list:
    await asyncio.sleep(1)
    return list(reversed(numbers))

async def main() -> list:
    task = asyncio.create_task(foo([1, 2, 3]), name="foo_task")

    # The result of the wrapped coroutine
    result_coro = await task

    # Return the result of the Task
    # If the Task is done, the result of the wrapped coroutine is returned (or if the coroutine raised an exception, 
    # that exception is re-raised.) If the Task has been cancelled, this method raises a CancelledError exception. If 
    # the Task’s result isn’t yet available, this method raises a InvalidStateError exception.
    result_task = task.result()
    
    return result_task

result = asyncio.run(main())
print(result)