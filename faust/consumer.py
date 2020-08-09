import asyncio
import json
from contextvars import ContextVar
from random import randint
from faust import App, Topic, Sensor
from faust.types import TP

t_offset = ContextVar('offset')

class MySensor(Sensor):
    def on_message_in(self, tp, offset, message):
        print(f'in {offset}')
        t_offset.set(offset)

    def on_message_out(self, tp, offset, message) -> None:
        print(f'out {offset}')

    # def on_commit_initiated(self, consumer):
    #     print(f'on_commit_initiated {consumer}')

    # def on_commit_completed(self, consumer, state):
    #     print(f'on_commit_completed {consumer}, {state}')

app = App('the_producer', broker='kafka://localhost', value_serializer='raw')
app.sensors.add(MySensor())
# app.client_only = True
t = app.topic('change_table', 
        # acks=False, 
        partitions=1,
    )

@app.agent(t)
async def consumer(stream):
    cache = []
    async for v in stream:
        print(f'{t_offset.get()}: {v}')
        cache.append((t_offset.get(), v))

        if len(cache) > 10:
            print([t[0] for t in cache])
            cache = []
            await asyncio.sleep(3)

# @app.timer(3)
# async def commit():
#     print('commit')
#     if t not in app.topics:
#         app.topics.add(t)

#     await app.commit('change_table')
    # await app.commit(None)
    # for topic in app.topics:
    #     print(topic)
    # print('change_table' in app.topics)

if __name__ == "__main__":
    app.main()