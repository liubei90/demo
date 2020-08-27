import json
from random import randint, sample, random
from faust import App, Topic

app = App('the_producer', broker='kafka://localhost', value_serializer='raw')
app.producer_only = True
t = app.topic('gyl_saas_dev')

# @app.task
# async def push_data_to_kafka():
#     await create_change2()

@app.timer(0.5)
async def push_data_to_kafka():
    await create_change()

# @app.timer(3)
# async def echo():
    # print('echo...')

@app.on_produce_message.connect
def on_produce(app, signal, key, value, partition, timestamp, headers):
    print(f'{key}, {value}, {partition}')


tables = {
    'd_supplier_agile': ['supplier_name', 'merchant_type'],
    'd_supplier_property_status': ['supplier_id', 'field1', 'field2'],
    'd_supplier_contact': ['supplier_id', 'name'],
}

def get_random_str(l=5):
    return ''.join(sample('abcdefghijklmnopqrstuvwxyz1234567890', l))

def get_column_template(name, value=get_random_str(), is_update=True if random() > 0.5 else False):
    return {
        "isNull": False,
        "name": name,
        "isKey": False,
        "index": 0,
        "value": value,
        "isUpdate": is_update
    }

async def create_change():
    supplier_id='123123123'
    table_name='d_supplier_property_status'

    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    await t.send(value=json.dumps(c1))

def _create_change2(table_name, event_type, after, before=[]):
    return {
        "afterColumns": after,
        "instance": "ykj_tqdzh",
        "beforeColumns": before,
        "dbName": "mycommunity_poly",
        "extractTime": "2020-06-11 22:01:07",
        "eventType": event_type,
        "tableName": table_name,
        "executeTime": "2020-06-11 22:00:24"
    }

async def create_change2():
    # 从表更新 -> 更新
    supplier_id='123123123'
    table_name='d_supplier_property_status'

    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id + '_new', is_update=True),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ], [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=True),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))


    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    c2 = _create_change2(table_name, 'DELETE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id + '_new', is_update=True),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))


async def yyy_create_change2():
    # 从表更新 -> 更新
    supplier_id='123123123'
    table_name='d_supplier_property_status'

    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))


    supplier_id='123123123qqq'
    table_name='d_supplier_property_status'

    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        get_column_template('field1', value=get_random_str(), is_update=False),
        get_column_template('field2', value=get_random_str(), is_update=True),
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))


async def yyy_create_change2():
    # 主表新增 -> 更新 -> 更新
    id='123123123'
    table_name='d_supplier_agile'
    columns=['supplier_name', 'merchant_type']

    c1 = _create_change2(table_name, 'INSERT', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))

    # 从表新增 -> 更新 -> 更新
    supplier_id='123123123'
    table_name='d_supplier_property_status'
    columns=['field1', 'field2']

    c1 = _create_change2(table_name, 'INSERT', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value='d_supplier_property_status_id', is_update=False),
        get_column_template('supplier_id', value=supplier_id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))


async def yyy_create_change2():
    id='123123123'
    table_name='d_supplier_agile'
    columns=['supplier_name', 'merchant_type']
    # 主表新增 -> 更新 -> 更新
    c1 = _create_change2(table_name, 'INSERT', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))


    # 新增 -> ... -> 删除
    c1 = _create_change2(table_name, 'INSERT', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c4 = _create_change2(table_name, 'DELETE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))
    await t.send(value=json.dumps(c4))


    #删除 -> ... -> 新增
    c1 = _create_change2(table_name, 'DELETE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c4 = _create_change2(table_name, 'INSERT', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))
    await t.send(value=json.dumps(c4))


    # 修改 -> 修改
    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c3 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))
    await t.send(value=json.dumps(c3))

    # 修改 -> 删除
    c1 = _create_change2(table_name, 'UPDATE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    c2 = _create_change2(table_name, 'DELETE', [
        get_column_template('id', value=id, is_update=False),
        *[ get_column_template(c) for c in columns ]
    ])
    await t.send(value=json.dumps(c1))
    await t.send(value=json.dumps(c2))



if __name__ == "__main__":
    app.main()
