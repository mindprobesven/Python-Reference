#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# Event
#
# An asyncio event can be used to notify multiple asyncio tasks that some event has happened.
#
# An Event object manages an internal flag that can be set to true with the set() method and reset to false with 
# the clear() method. The wait() method blocks until the flag is set to true. The flag is set to false initially.
#
# ----------------------------------------------------------------------------------------------------------------

import asyncio

async def run_when_event_is_set(event: asyncio.Event):
    print('Waiting for event...')
    await event.wait()
    print('Got the event, start running!')
    await asyncio.sleep(1)
    print('run_when_event_is_set Done')

async def stop_when_event_is_set(event: asyncio.Event):
    print('Waiting for event to be set')
    while True:
        if event.is_set():
            print('Event set caught, breaking the while loop')
            break
        await asyncio.sleep(1)
    print('stop_when_event_is_set Done')

async def main():
    # Create the Event object
    event = asyncio.Event()

    # This task uses event.wait() and blocks the coroutine until the flag is set to true
    task1 = asyncio.create_task(run_when_event_is_set(event), name="Task 1")
    # This task is running a while loop which queries event.is_set(). It will break the while loop when the event was set
    task2 = asyncio.create_task(stop_when_event_is_set(event), name="Task 2")

    print('Tasks started')

    # Shows all tasks are running
    for task in asyncio.all_tasks():
        print(task)

    # We wait for 1 seconds and then set the event
    await asyncio.sleep(1)
    event.set()

    # We wait until all tasks are done
    await asyncio.gather(task1, task2, return_exceptions=True)

    # Shows all tasks are done
    for task in asyncio.all_tasks():
        print(task)

if __name__ == "__main__":
    asyncio.run(main())
    print('Done')