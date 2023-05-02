import sys
import asyncio
import aiohttp


COUNT = 0


async def fetch_url(url, semaphore):
    async with aiohttp.ClientSession() as session:
        async with semaphore:
            async with session.get(url) as resp:
                if resp.status == 200:
                    global COUNT
                    COUNT += 1


async def function(numbers, files):
    urls = []
    with open(files, "r") as file:
        for line in file:
            urls.append(line.rstrip())

    num = asyncio.Semaphore(numbers)
    tasks = [asyncio.create_task(fetch_url(url, num)) for url in urls]
    await asyncio.gather(*tasks)


def main():
    cli = sys.argv[1:]
    asyncio.run(function(int(cli[-2]), cli[-1]))


main()
