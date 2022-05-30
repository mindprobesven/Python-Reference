#!/usr/bin/env python3

# ---------------------------------------------------------------------------------------------------------------
# with - Creating Custom Context Managers - Aync
#
# To create an asynchronous context manager, you need to define the .__aenter__() and .__aexit__() methods.
# ----------------------------------------------------------------------------------------------------------------

import asyncio
import aiohttp


class AsyncSession:
    def __init__(self, url):
        self._url = url

    # In .__aenter__(), you create an aiohttp.ClientSession(), await the .get() response, and finally return the 
    # response itself.
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    # In .__aexit__(), you close the session, which corresponds to the teardown logic in this specific case.
    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()

async def check(url):
    # Note that .__aenter__() and .__aexit__() must return awaitable objects. In other words, you must define them 
    # with async def, which returns a coroutine object that is awaitable by definition.
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

if __name__ == "__main__":
    asyncio.run(main())
