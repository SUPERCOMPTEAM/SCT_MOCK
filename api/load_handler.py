import random

from aiohttp import web

from statistic.monitoring import Load
from statistic.statistic import Statistic


class LoadHandler:
    def __init__(self, number):
        self.number = number
        self.statistic = Statistic()

    async def load_random(self, request):
        load_type = random.choice(list(Load))
        await self.statistic.make_load(load_type)
        return web.Response(text="load from server " + str(self.number))
