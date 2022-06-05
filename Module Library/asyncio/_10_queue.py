#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Queues
#
# This example explains how to use asyncio.Queue()
#
# A first in, first out (FIFO) queue.
# If maxsize is less than or equal to zero, the queue size is infinite. If it is an integer greater than 0, then 
# await put() blocks when the queue reaches maxsize until an item is removed by get().
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import random
import itertools as it

async def producer(queue: asyncio.Queue):
    number_messages = random.randint(4, 6)
    for _ in it.repeat(None, number_messages):
        # Add an item to the queue
        await queue.put(random.randint(1, 10))
        print(f'{asyncio.current_task().get_name()} added {number_messages} items to queue - Queue size: {queue.qsize()}')
    
    await asyncio.sleep(0.1)

async def consumer(queue: asyncio.Queue):
    while True:
        # Get an item from the queue
        queue_item = await queue.get()
        await asyncio.sleep(0.1)
        print(f'{asyncio.current_task().get_name()} took queue item {queue_item} - Queue size: {queue.qsize()}')
        # Notifies that queue that the item has been processed
        queue.task_done()

async def main():
    # Create the queue. We set it to maxsize=3
    queue = asyncio.Queue(maxsize=3)

    # We create 2 producer tasks. These producers at more items to the queue than the maxsize of 3, to show what happens
    # when the queue is full. In that case the producer will wait until a free slot is available before adding item.
    producer_tasks = [asyncio.create_task(producer(queue), name=f'Producer-{n}') for n in range(2)]

    # We create 2 consumer tasks that each take one item from the queue every 0.1 seconds
    consumer_tasks = [asyncio.create_task(consumer(queue), name=f'Consumer-{n}') for n in range(2)]

    # This will complete when all producers have added their items to the queue
    await asyncio.gather(*producer_tasks)
    print('All producer tasks are done')

    # This will complete when the queue is fully processed and empty
    await queue.join()
    print('All items in the queue have been processed')

    # At this point, if we check what tasks are still running, we see that the consumer tasks are still running because
    # they run a while loop
    for task in asyncio.all_tasks():
        print(task)

    # Since the consumer tasks are still running, we cancel them
    for task in consumer_tasks:
        task.cancel()
        print(f'{task.get_name()} cancelling...')

    # At this point, if we check the running tasks, we see that consumer tasks are now wait_for=<Future cancelled>
    for task in asyncio.all_tasks():
        print(task)

    # We use gather() to wait until consumer tasks are cancelled
    # We must use return_exceptions=True so exceptions are treated the same as successful results, otherwise the first 
    # raised exception (CancelledError) is immediately propagated to the task that awaits on gather()
    await asyncio.gather(*consumer_tasks, return_exceptions=True)
    print('All consumer tasks are done')

    # At this point, if we check the running tasks, we see that the consumer tasks are done
    for task in asyncio.all_tasks():
        print(task)

if __name__ == "__main__":
    asyncio.run(main())
    print('Done')