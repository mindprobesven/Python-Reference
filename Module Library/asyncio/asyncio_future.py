#!/usr/bin/env python3

import sys
import time
import threading
import asyncio

class SpeedTest(threading.Thread):
    __THREAD_NAME = "SpeedTestThread"
    __IS_DAEMON = True

    def __init__(self, group=None, target=None, name=__THREAD_NAME,
                 args=(), kwargs=None, daemon=__IS_DAEMON):
        super().__init__(group=group, target=target, name=name, daemon=daemon)

        self.event_loop = asyncio.new_event_loop()
        threading.Thread(name='EventLoopThread', target=self._event_loop_thread, args=(self.event_loop,), daemon=True).start()

        self.start()

    def run(self):
        print(f"+ [{threading.currentThread().name}] - [run] - {time.strftime('%X')}")
        result = self._connect()

        if result == 1:
            print(f"+ [{threading.currentThread().name}] - [run] - {time.strftime('%X')}")
            self._listen()

        while True:
            print(f"+ [{threading.currentThread().name}] - [run] - {time.strftime('%X')}")
            time.sleep(1.0)

    def _event_loop_thread(self, loop):
        print("Starting event loop")
        asyncio.set_event_loop(loop)
        loop.run_forever()

        loop.close()
        print("Exit!")

    def _connect(self):
        print(f"+ [{threading.currentThread().name}] - [_connect] - {time.strftime('%X')}")
        future = asyncio.run_coroutine_threadsafe(self._connect_coro(), self.event_loop)
        return future.result()

    async def _connect_coro(self):
        print(f"++ [{threading.currentThread().name}] - [_connect_coro] - {time.strftime('%X')}")
        await asyncio.sleep(4.0)
        return 1

    def _listen(self):
        print(f"+ [{threading.currentThread().name}] - [_listen] - {time.strftime('%X')}")
        asyncio.run_coroutine_threadsafe(self._listen_coro(), self.event_loop)

    async def _listen_coro(self):
        while True:
            print(f"++ [{threading.currentThread().name}] - [_listen_coro] - {time.strftime('%X')}")
            await asyncio.sleep(1.0)

if __name__ == "__main__":
    try:
        speed_test = SpeedTest()

        while True:
            print(f"[{threading.currentThread().name}] - {time.strftime('%X')}")
            time.sleep(1.0)
    except KeyboardInterrupt:
        sys.exit('\nInterrupted by user')
