import json
from random import randint, sample, random
from faust import App, Topic, web

from ids import get_id
from tloginligids import get_id as get_login_id

app = App('the_producer', broker='kafka://localhost', value_serializer='raw')
app.producer_only = True
t = app.topic('local_test')
manage_blueprint = web.Blueprint('manage')

@manage_blueprint.route('/send', name='send')
class RefreshContent(web.View):
    async def get(self, request: web.Request) -> web.Response:
        c = await create_change3()
        await t.send(value=json.dumps(c))
        return self.json(c)

@manage_blueprint.route('/send/t_login_log', name='send_t_login_log')
class SendTLoginLog(web.View):
    async def get(self, request: web.Request) -> web.Response:
        c = await create_t_login_log()
        await t.send(value=json.dumps(c))
        return self.json(c)

@manage_blueprint.route('/send/t_data_change_log', name='send_t_data_change_log')
class SendTLoginLog(web.View):
    async def get(self, request: web.Request) -> web.Response:
        c = await create_t_data_change_log()
        await t.send(value=json.dumps(c))
        return self.json(c)

@manage_blueprint.route('/send/t_data_change_detail_log', name='send_t_data_change_detail_log')
class SendTLoginLog(web.View):
    async def get(self, request: web.Request) -> web.Response:
        c = await create_t_data_change_detail_log()
        await t.send(value=json.dumps(c))
        return self.json(c)

manage_blueprint.register(app, url_prefix='/')

# @app.task
# async def push_data_to_kafka():
#     await create_change3()

# @app.timer(0.5)
# async def push_data_to_kafka():
#     await create_change3()

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

def _create_change2(dbName, table_name, event_type, after, before=[]):
    return {
        "afterColumns": after,
        "instance": "ykj_tqdzh",
        "beforeColumns": before,
        "dbName": dbName,
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


async def create_change3():
    '''
    id,
    code,
	name,
	proj_id,
	proj_name
    '''
    c = _create_change2('mycommunity_retesting', 'dw_com_dim_t_building', 'INSERT', [
        get_column_template('id', value=get_id(), is_update=False),
        get_column_template('code'),
        get_column_template('name'),
        get_column_template('proj_id'),
        get_column_template('proj_name'),
    ])

    # c = _create_change2(table_name, 'UPDATE', [
    #     get_column_template('id', value='d_supplier_property_status_id', is_update=False),
    #     get_column_template('supplier_id', value=supplier_id, is_update=False),
    #     get_column_template('field1', value=get_random_str(), is_update=False),
    #     get_column_template('field2', value=get_random_str(), is_update=True),
    # ])

    # c = _create_change2(table_name, 'DELETE', [
    #     get_column_template('id', value=id, is_update=False),
    #     *[ get_column_template(c) for c in columns ]
    # ])

    # await t.send(value=json.dumps(c))

    return c

async def create_t_login_log():
    '''
    id,
	user_id,
	source,
	current_url,
	referer_url,
	user_agent,
	outer_ip,
	created_on
    '''
    c = _create_change2('mycommunity_logcenter', 't_login_log', 'INSERT', [
        get_column_template('id', value=get_login_id(), is_update=False),
        get_column_template('user_id'),
        get_column_template('source'),
        get_column_template('current_url'),
        get_column_template('referer_url'),
        get_column_template('user_agent'),
        get_column_template('outer_ip'),
        get_column_template('created_on'),
    ])

    return c


def get_change_log_id():
    change_log_ids = [
        "39f519e2-943a-5727-0b4e-a568e2e00a6c",
        "39f519f4-9da7-b0fb-cb44-6b263b237cb9",
        "39f519fe-f257-6d9c-1e3d-ebb06400a5dc",
        "39f519fe-f314-fd04-ad58-5b630b4585f7",
        "39f51a00-369f-d125-c7a6-525702ad815d",
        "39f51a01-6541-4e07-b555-24cb89992363",
        "39f51a01-72f7-d1a3-1cb5-395b1ce0a016",
        "39f51a05-3db9-1f41-9781-29bb38942e10",
        "39f51a05-9dd9-ce7b-bbc1-cf4d53a2a3ea",
        "39f51a06-6af5-9606-5da3-ea54cca077a9",
        "39f51a07-308a-c5b1-3f72-7b5751004e69",
        "39f51a08-5494-da36-c743-1193b45bbe7b",
        "39f51a08-77c4-53d0-c5e2-5ff3c67650d7",
        "39f51a08-96a1-994f-219a-29b356ae657a",
        "39f51a08-c375-a664-c828-30c600a4e121",
        "39f51a0c-4a84-5f19-da3f-5a27fcd4f150",
        "39f51a0e-e210-6143-88d6-bb923b765306",
        "39f51a10-fedc-0d3e-afcf-bf33e08a3a22",
        "39f51a12-73c3-7735-0afe-7621543d2fc0",
        "39f51a12-94a0-4be3-5228-727d78060c60",
        "39f51a12-bcf6-89ee-c907-3e62d2ea1d59",
        "39f51a13-907e-5058-2729-8e74872d511f",
        "39f51a13-b5ad-f880-2b2a-2c8c7c7b0d61",
        "39f51a14-2700-edd5-fe6f-e6d0210d8d17",
        "39f51a14-3b49-828f-68b9-d56b7b39f5dc",
        "39f51a15-52ae-f6bc-3679-241d63dbc356",
        "39f51a17-6f3b-e642-9652-1d6ff6c46748",
        "39f51a19-dfd9-5280-7dfd-da0aa44487cc",
        "39f51a24-6600-1d1e-9884-45cfa3962196",
        "39f51a26-f17a-1bec-784f-aa148dd49f78"]

    return change_log_ids[randint(0, len(change_log_ids))]



async def create_t_data_change_log():
    '''
    id,
	user_id,
	object_name
    '''
    c = _create_change2('mycommunity_logcenter', 't_data_change_log', 'INSERT', [
        get_column_template('id', value=get_change_log_id(), is_update=False),
        get_column_template('user_id')
    ])

    return c

async def create_t_data_change_detail_log():
    '''
    id,
	user_id,
	object_name
    '''
    c = _create_change2('mycommunity_logcenter', 't_data_change_detail_log', 'UPDATE', [
        get_column_template('id', is_update=False),
        get_column_template('change_id', value=get_change_log_id(), is_update=False),
        get_column_template('object_name')
    ])

    return c


if __name__ == "__main__":
    app.main()
