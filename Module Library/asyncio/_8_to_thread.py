#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# to_thread()
#
# Run coroutines and normal blocking IO functions concurrently.
# The blocking IO functions run in a separate thread.
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import time

# ----------------------------------------------------------------------------------------------------------------
# asyncio.to_thread was added in Python 3.9
# Older versions have to manually add this method
import functools
import contextvars

async def to_thread(func, /, *args, **kwargs):
    """Asynchronously run function *func* in a separate thread.
    Any *args and **kwargs supplied for this function are directly passed
    to *func*. Also, the current :class:`contextvars.Context` is propagated,
    allowing context variables from the main thread to be accessed in the
    separate thread.
    Return a coroutine that can be awaited to get the eventual result of *func*.
    """
    loop = asyncio.events.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)
# ----------------------------------------------------------------------------------------------------------------

def blocking_io_func(*args, **kwargs):
    print(f"start blocking_io_func at {time.strftime('%X')}")

    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    time.sleep(1)
    print(f"blocking_io_func complete at {time.strftime('%X')}")
    return 'blocking_io_func done'

async def coroutine_func():
    print(f"start coroutine_func at {time.strftime('%X')}")
    await asyncio.sleep(1.0)
    print(f"coroutine_func complete at {time.strftime('%X')}")
    return 'coroutine_func done'

async def main():
    # task1 is a coroutine
    task1 = asyncio.create_task(coroutine_func(), name='coroutine_function_task')
    # task2 is a blocking IO function. To run in concurrently with the coroutine task1, we use asyncio.to_thread() 
    # to run it in a separate thread.
    task2 = to_thread(blocking_io_func, (1, 2), name='Sven', age=42)

    results = await asyncio.gather(task1, task2)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())