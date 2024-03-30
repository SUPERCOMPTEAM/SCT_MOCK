from aiohttp import web


class Stupid:
    def __init__(self, number):
        self.number = number

    async def hello(self, request):
        return web.Response(text="hello from server " + str(self.number))
