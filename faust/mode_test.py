from typing import List
import os
import io
import sys
import asyncio
import random
import pydot
from mode import Service, worker
from mode.worker import Worker

class EchoSecond(Service):
    count: int

    @Service.task
    async def _echo(self) -> None:
        while not self.should_stop:
            print(self.count)
            await asyncio.sleep(1)
            self.count += 1

    # @Service.timer(1)
    # async def _echo(self) -> None:
    #     while not self.should_stop:
    #         print(self.count)
    #         self.count += 1

    async def on_started(self) -> None:
        self.count = random.randint(1, 100)

class App(Service):
    echo_serv: EchoSecond
    echo_servs: List[EchoSecond] = []

    def __post_init__(self) -> None:
        self.echo_serv = EchoSecond(loop=self.loop)
        self.add_dependency(self.echo_serv)

        # for i in range(10):
        #     serv = EchoSecond(loop=self.loop)
        #     self.echo_servs.append(serv)
        #     self.add_dependency(serv)

    async def on_started(self) -> None:
        print('app.on_started')
        await asyncio.sleep(5)
        self.print_graph('image1.png')

        # 移除依赖
        await self.remove_dependency(self.echo_serv)
        await self.echo_serv.stop()

        runtime_serv = EchoSecond(loop=self.loop)
        # 添加运行时依赖
        await self.add_runtime_dependency(runtime_serv)
        await asyncio.sleep(5)
        self.print_graph('image2.png')

        await self.remove_dependency(runtime_serv)
        await runtime_serv.stop()

        runtime_serv = EchoSecond(loop=self.loop)
        await runtime_serv.start()

        await asyncio.sleep(5)
        self.print_graph('image3.png')

    def print_graph(self, img_path) -> None:
        o = io.StringIO()
        beacon = self.beacon.root or self.beacon
        beacon.as_graph().to_dot(o)
        graph, = pydot.graph_from_dot_data(o.getvalue())

        with open(img_path, 'wb') as fh:
            fh.write(graph.create_png())

    @Service.timer(1)
    async def time_task(self):
        print('app.time_task')

async def amain():
    app = App()
    await app.start()

def main():
    Worker(
        App(), 
        debug=True,
        loglevel='INFO', 
        # logfile=sys.stdout, 
        # daemon=False
    ).execute_from_commandline()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(amain())

if __name__ == "__main__":
    main()
