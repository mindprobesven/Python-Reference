#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Threading - run_coroutine_threadsafe() and call_soon_threadsafe()
#
# This example explains how to run coroutine and normal blocking IO functions in a separate thread.
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import concurrent.futures
import threading
import time
from threading import Thread

def thread_function(loop):
    # Set and run the new asyncio event loop inside the thread until it is manually stopped with .stop()
    asyncio.set_event_loop(loop)
    print("Event loop started")
    loop.run_forever()

    # This executes after the asyncio event loop is stopped with .stop()
    print("Event loop stopped")
    print(f"Loop: {loop}") # loop running = false, closed = false

    # Close the event loop
    loop.close()
    print("Closed event loop")
    print(f"Loop: {loop}") # loop running = false, closed = true

    # Since the asyncio event loop is finished, the thread will also finish and exit here
    print("Thread finished! Exit thread.")

def blocking_io_func(arg, future):
    print(f"start blocking_io_func at {time.strftime('%X')}")
    time.sleep(1)
    print(f"blocking_io_func complete at {time.strftime('%X')}")
    # We set the future to return the result
    future.set_result('blocking_io_func done')

async def coroutine_func(*args, **kwargs):
    print(f"start coroutine_func at {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(f"coroutine_func complete at {time.strftime('%X')}")
    return 'coroutine_func done'

async def main():
    # Here we create a new asyncio event loop that will run in the new thread
    new_asyncio_event_loop = asyncio.new_event_loop()

    # We create the new thread and pass to it the new asyncio event loop (new_asyncio_event_loop). It will be set to
    # run in the new thread
    new_thread = Thread(name="New Thread", target=thread_function, args=(new_asyncio_event_loop,))
    new_thread.start()
    
    # We list the currently existing threads
    for thread in threading.enumerate():
        print(thread)   # The main thread and new thread are running
    
    # This shows how to run a coroutine function in the new asyncio event loop
    # ----------------------------------------------------------------------------------------------------------------
    # We use run_coroutine_threadsafe() to submit a coroutine to the new event loop. It returns a 
    # concurrent.futures.Future to access the result.
    task1 = asyncio.run_coroutine_threadsafe(coroutine_func(1, name='foo'), new_asyncio_event_loop)
    result = task1.result()
    print(result)

    # This shows how to run a normal blocking IO function in the new asyncio event loop and how to return its result
    # ----------------------------------------------------------------------------------------------------------------
    # We use call_soon_threadsafe(), which can schedule a callback function from another thread. Or in other words, run a
    # normal blocking IO function in the new asyncio event loop.
    # 
    future = concurrent.futures.Future()
    # Here we schedule the callback (blocking_io_func) to run in the new asyncio event loop. To be able to return its
    # result, we must create a future, pass it to the callback and then set it.
    new_asyncio_event_loop.call_soon_threadsafe(blocking_io_func, 1, future)
    # This waits for the future to be set in the callback with a timeout of 10 seconds. If the future is set, the returned
    # result can be accessed in future.result()
    result = future.result(10)
    print(result)

    print('-' * 50)

    # Since the new asyncio event loop is set to run_forever(), it has to be stopped manually at the end. Using
    # new_asyncio_event_loop.stop() would not work since it is running in the new thread. We have to use
    # call_soon_threadsafe() to schedule this callback from the new thread.
    new_asyncio_event_loop.call_soon_threadsafe(new_asyncio_event_loop.stop)

    new_thread.join()    

if __name__ == "__main__":
    asyncio.run(main())
    print('Done')
