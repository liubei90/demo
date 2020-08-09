import json
from random import randint
from faust import App, Topic

app = App('the_producer', broker='kafka://localhost', value_serializer='raw')
app.producer_only = True
t = app.topic('change_table')

@app.timer(1)
async def push_data_to_kafka():
    await t.send(value=json.dumps({ 'column': 'id', 'before': str(randint(1, 100000)) }))

# @app.timer(3)
# async def echo():
    # print('echo...')

@app.on_produce_message.connect
def on_produce(app, signal, key, value, partition, timestamp, headers):
    print(f'{key}, {value}, {partition}')

if __name__ == "__main__":
    app.main()