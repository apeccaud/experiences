import asyncio
import aiohttp


URL = 'https://api.github.com/events'


async def fetch(session):
    async with session.get(URL) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        futures = [fetch(session) for _ in range(10)]
        for i, future in enumerate(asyncio.as_completed(futures)):
            # Now we can process the API response as soon as it comes
            result = await future
            print(f'{i} fetched {len(result)} results')


asyncio.run(main())

