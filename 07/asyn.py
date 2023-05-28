import asyncio
import argparse
import re
from collections import Counter
import aiohttp
from bs4 import BeautifulSoup as BSoup


async def fetch_url(que):
    async with aiohttp.ClientSession() as session:
        while True:
            url = await que.get()
            async with session.get(url) as resp:
                if resp.status == 200:
                    tmp1 = await resp.text()
                    tmp2 = BSoup(tmp1, 'html.parser').text
                    tmp3 = re.findall(r'[a-z]+', tmp2, re.IGNORECASE)
                    tmp4 = dict(Counter(tmp3).most_common(5))
                    print(tmp4)
                    que.task_done()


async def produce(tmp1, tmp2):
    for line in tmp1:
        await tmp2.put(line.rstrip())


async def function(files, numbers):
    deq = asyncio.Queue()

    with open(files, 'r') as file_pointer:
        task_queue = asyncio.create_task(produce(file_pointer, deq))
        tasks = [asyncio.create_task(fetch_url(deq)) for i in range(numbers)]

        await task_queue
        await deq.join()


def main(tmp, cnt):
    asyncio.run(function(tmp, cnt))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-c",
                        help="count of simultaneous requests with option -c",
                        type=int)
    parser.add_argument("C", nargs='*', help="count of simultaneous requests",
                        type=int)
    parser.add_argument("file", help="name of file", type=str)
    temp = parser.parse_args()

    temp2 = temp.c if temp.c else temp.C[0]
    main(temp.file, temp2)
 
