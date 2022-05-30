#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Coroutines
#
# To actually run a coroutine, asyncio provides three main mechanisms.
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import time

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    start = time.perf_counter()

    # 2. Awaiting on a coroutine. These will run one after the other. Not concurrently.
    await say_after(1, "Hello")
    await say_after(2, "Sven")

    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    # 3. The asyncio.create_task() function to run coroutines "concurrently" as asyncio Tasks
    start = time.perf_counter()

    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "Sven"))

    await task1
    await task2

    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

if __name__ == "__main__":
    # 1. The asyncio.run() function to run the top-level entry point “main()” function
    asyncio.run(main())