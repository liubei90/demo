import asyncio

from utils import log
from es_mng import EsMng


async def get_es_info():
    es = EsMng()
    res = await es.request('/')
    log(res)


async def do_sth():
    await get_es_info()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_sth())


if __name__ == "__main__":
    main()
