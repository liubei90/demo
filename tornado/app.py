import time
import asyncio
from tornado import web

class IndexHandler(web.RequestHandler):
    async def get(self):
        return self.write({ 'status': True, 'msg': '请求成功' })


class SttHandler(web.RequestHandler):
    def post(self):
        with open(f'./pcm_{time.time()}', mode='wb+') as f:
            f.write(self.request.body)

        return self.write({ 'data': '这是测试数据' })


def create_app():
    print('create app success')
    app = web.Application([
        (r'/index', IndexHandler),
        (r'/stt', SttHandler),
    ])
    app.listen(8001)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    create_app()
    loop.run_forever()
