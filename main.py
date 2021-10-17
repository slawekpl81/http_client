import aiohttp
import asyncio
import argparse
from config import base, path, params, payload

parser = argparse.ArgumentParser()
parser.add_argument('--method', '-m')
args = parser.parse_args()
# print(args.method)


async def main_get(base=base, path=path, params=params):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{base}{path}',
                               params=params) as response:
            print(response.url)
            print(response.status)
            print(await response.text())


def get_method():
    asyncio.run(main_get())


def post_method():
    asyncio.run(main_post())


async def main_post(base=base, path=path, payload=payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{base}{path}',
                                json=payload) as response:
            print(response.url)
            print(response.status)
            print(await response.text())


methods = {
    'get': get_method,
    'post': post_method,
}

if __name__ == '__main__':
    methods[args.method]()

