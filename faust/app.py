import time
import asyncio
from faust.cli import argument
from faust import App, Sensor
from faust.types import TP

class MySensor(Sensor):
    def on_message_in(self, tp, offset, message):
        print(f'in {offset}')
        # print(type(tp))
        # print(dir(tp))
        # # print('tp.count()')
        # # print(tp.count())
        # print(type(message))
        # print(message.topic)
        # print(message.partition)
        # print(message.offset)
        # print(message.headers)
        # print(message.checksum)
        # print(message.refcount)
        

    def on_message_out(self, tp, offset, message):
        # print(f'out {offset}')
        pass

app = App('page_views', broker='kafka://localhost:9092', value_serializer='raw')
app.sensors.add(MySensor())

page_views = app.topic('page_views')

count = 0

async def process_data(d):
    global count
    count += 1
    await asyncio.sleep(0.02)

async def batch_process_data(ds):
    global count
    for d in ds:
        if count % 3 == 0:
            count += 1
            continue
        await process_data(d)

@app.agent(page_views)
async def receive_change(change_logs):
    # print(type(change_logs))
    # print(type(change_logs.channel))
    # print(change_logs)
    # print(len(change_logs))

    # print(type(page_views))

    # print(page_views == change_logs.channel)

    print(type(app.consumer))

    res = await app.consumer.highwaters(TP('page_views', 0))
    print(res)

    # subscriber_count

    cache_data = []
    async for change in change_logs:
        await asyncio.sleep(1000)

        # cache_data.append(change)
        # for c in change:
        #     cache_data.append(process_data(c))
        # await asyncio.gather(*cache_data)
        # cache_data = []

        # if len(cache_data) > 1000:
        #     await asyncio.gather(*cache_data)
        #     # await batch_process_data(cache_data)
        #     cache_data = []


# @app.timer(1)
# async def print_count():
#     print(time.strftime('%H:%M:%S', time.localtime()), count)
#     # print(count)

@app.command(
    # argument('send_count', type=int)
)
async def msend():
    # await receive_change.send(value='test...')
    send_count = 1000
    tasks = []
    for i in range(send_count):
        tasks.append(receive_change.send(value=f'msg: {str(i)}'))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    app.main()
