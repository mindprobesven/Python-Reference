#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# async IO
#
# asyncio is a library to write concurrent code using the async/await syntax.
#
# async IO is not threading, nor is it multiprocessing. It is not built on top of either of these. 
# In fact, async IO is a single-threaded, single-process design: it uses cooperative multitasking.
#
# At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function.
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def count():
    print("One")
    # The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding 
    # coroutine.)
    await asyncio.sleep(1)
    print("Two")

# The syntax async def introduces either a native coroutine or an asynchronous generator.
async def main():
    # Return a future aggregating results from the given coroutines/futures.
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    # Execute the coroutine and return the result.
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")