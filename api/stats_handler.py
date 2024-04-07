from aiohttp import web

from statistic.statistic import Statistic


class StatsHandler:
    def __init__(self):
        self.statistic = Statistic()

    async def get_stats(self, request):
        return web.json_response({"completed": self.statistic.completed,
                                  "overload": self.statistic.overload,
                                  "downtime": self.statistic.downtime})
