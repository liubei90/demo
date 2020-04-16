import asyncio
from tornado import web

class IndexHandler(web.RequestHandler):
    async def get(self):
        return self.write({ 'status': True, 'msg': '请求成功' })


def create_app():
    print('create app success')
    app = web.Application([
        (r'/index', IndexHandler)
    ])
    app.listen(8100)

def set_interval(fn, t = 1):
    loop = asyncio.get_running_loop()
    fn()
    loop.call_later(t, set_interval, fn, t)


has_app = False
count = 0
def loop_fun():
    global has_app
    global count
    count += 1
    print(count)
    if count > 10 and not has_app:
        has_app = True
        create_app()

async def main():
    global count
    global has_app
    set_interval(loop_fun, 1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
