import time
import asyncio
from tornado import web

class IndexHandler(web.RequestHandler):
    async def get(self):
        return self.write({ 'status': True, 'msg': '请求成功' })


class SttHandler(web.RequestHandler):
    async def post(self):
        with open(f'./pcm_{time.time()}', mode='rb', encoding='utf8') as f:
            f.write(self.request.body)


def create_app():
    print('create app success')
    app = web.Application([
        (r'/index', IndexHandler),
        (r'/stt', SttHandler),
    ])
    app.listen(8100)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    create_app()
    loop.run_forever()
