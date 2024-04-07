import asyncio

from aiohttp import web

from statistic.statistic import Statistic


class StupidHandler:
    def __init__(self, number):
        self.number = number
        self.statistic = Statistic()

    async def hello(self, request):
        self.statistic.start_process()
        self.statistic.end_process()
        return web.Response(text="hello from server " + str(self.number))
