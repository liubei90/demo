import json
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from config import get_config
from utils import log


class EsMng():
    def __init__(self, timeout=10):
        self._es_config = get_config()['es']
        self._timeout = timeout
        self._origin_url = self._es_config['host']
        self._headers = {'Content-Type': 'application/json'}

    async def request(self, uri, method='GET', body=None, timeout=None):
        url = self._origin_url + uri
        request_body = body

        if type(body) in [dict, list]:
            request_body = json.dumps(body if body != None else {}, ensure_ascii=False)

        request_timeout = timeout if timeout != None else self._timeout
        req = HTTPRequest(url, method, body=request_body, request_timeout=request_timeout, headers=self._headers, auth_username=self._es_config['user'], auth_password=self._es_config['password'])

        try:
            client = AsyncHTTPClient()
            resp = await client.fetch(req)
            ret = None
            if resp.code in [200, 201]:
                ret = json.loads(resp.body)
                return ret

            raise Exception(resp)
        except Exception as e:
            log(e.message)
            raise e

    async def add_document(self, index_name, body=None, timeout=None):
        return await self.request('/%s/_doc' % (index_name,), method='POST', body=body, timeout=timeout)

    async def delete_by_query(self, index_name, body=None, timeout=None):
        return await self.request('/%s/_delete_by_query' % (index_name,), method='POST', body=body, timeout=timeout)

    async def update_by_query(self, index_name, body=None, timeout=None):
        return await self.request('/%s/_update_by_query' % (index_name,), method='POST', body=body, timeout=timeout)

    async def bulk_add_document(self, index_name, data=[], timeout=None):
        action = { 'index': { '_index': index_name, '_type': 'default' } }
        body = []

        for d in data:
            body.append(json.dumps(action))
            body.append(json.dumps(d))

        body = '\n'.join(body)
        body += '\n'
        return await self.request('/_bulk', method='POST', body=body, timeout=timeout)


def update_number_is_zero(res):
    if type(res) is dict:
        return 'updated' in res and res['updated'] == 0

def delete_number_is_zero(res):
    if type(res) is dict:
        return 'deleted' in res and res['deleted'] == 0
