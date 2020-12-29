import asyncio
import traceback
from pymysql.err import OperationalError
from aiomysql import connect

g_connection = None


async def ensure_connect():
    global g_connection
    g_connection = await connect('localhost', user='root', password="root", db='demo')


async def start():
    while True:
        cli = input('_>:')
        args = input('args:')

        if hasattr(g_connection, cli):
            f = getattr(g_connection, cli)
            try:
                res = None

                if not args:
                    res = f()
                else:
                    print([arg if arg not in ['True', 'False'] else (True if arg == 'True' else False) for arg in args.split('|')])
                    res = f(*[arg if arg not in ['True', 'False'] else (True if arg == 'True' else False) for arg in args.split('|')])

                if asyncio.iscoroutine(res):
                    res = await res
                
                print('res:')
                print(res)
            except OperationalError as e:
                print(e.args)
                print(e.args[0])
                print(type(e.args[0]))
                # print(traceback.format_exc())
            except Exception as e:
                print(type(e))
                print(e.__dict__)
                print(traceback.format_exc())


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ensure_connect())
    loop.run_until_complete(start())


if __name__ == "__main__":
    main()
