from aiohttp import web

from statistic.statistic import Statistic


class StatsHandler:
    def __init__(self):
        self.statistic = Statistic()

    async def get_current_stats(self, request):
        downtime, overload, completed = self.statistic.get_stats()
        return web.json_response({"completed": completed,
                                  "overload": overload,
                                  "downtime": downtime})
