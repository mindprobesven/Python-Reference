#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Request a Task to be cancelled
#
# This arranges for a CancelledError exception to be thrown into the wrapped coroutine on the next cycle of the 
# event loop. The coroutine then has a chance to clean up or even deny the request by suppressing the exception 
# with a try … … except CancelledError … finally block.
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def foo(numbers: list) -> list:
    try:
        await asyncio.sleep(5)      
        return list(reversed(numbers))
    except asyncio.CancelledError:
        print('foo(): exception CancelledError caught')
        # Use raise to propagate the CancelledError up to main()
        raise
    finally:
        print('foo(): after sleep optional cleanup')
    

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

    # task1 takes 5 seconds to be done. We will cancel it after only 2 seconds with task1.cancel()
    await asyncio.sleep(8)
    print("main(): Canceling task1 now")
    # This will cause a CancelledError exception to be thrown into the wrapped coroutine on the next cycle of the 
    # event loop
    task1.cancel()

    try:
        result = await task1
        print(result)
    except asyncio.CancelledError:
        # CancelledError was propagated up to main() via raise in the wrapped coroutine
        print("main(): task1 is cancelled now")

    await task2

    # Here we are trying to return the result of task1 using result(). If the task has been cancelled, which it was, 
    # this method raises a CancelledError exception.
    try:
        print(task1.result())
    except asyncio.CancelledError:
        print("main(): task1 is cancelled now")

    print("Done")

if __name__ == "__main__":
    asyncio.run(main())