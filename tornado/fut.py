import asyncio

async def aiorange(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 所有await _fut的协程都会被阻塞，且会在_fut被返回后的循环内被同时执行
_fut = None
index = 1
async def waite_fut():
    global _fut
    
    if _fut is None:
        loop = asyncio.get_running_loop()
        _fut = loop.create_future()
        await asyncio.sleep(1)
        print('1s')
        await asyncio.sleep(2)
        print('2s')
        await asyncio.sleep(3)
        print('3s')
        _fut.set_result(None)
        _fut = None
    else:
        print('waite the _fut')
        await _fut

async def main():
    global index
    async for i in aiorange(1):
        await waite_fut()
        print(i)
    print(index)
    index += 1

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(main(), main(), main(), main(), main()))