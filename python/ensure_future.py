import asyncio
import signal

count = 1

async def main(loop):
    global count
    print(count)
    await asyncio.sleep(1)
    asyncio.ensure_future(main(loop), loop=loop)
    count += 1

def handler_term():
    print('handler_term')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.add_signal_handler(signal.SIGTERM, handler_term)
    signal.signal(signal.SIGTERM, handler_term)
    # asyncio.ensure_future(main(loop), loop=loop)
    # loop.run_forever()
    loop.run_until_complete(main(loop))