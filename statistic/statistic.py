from statistic.monitoring import Monitoring, Load
import asyncio


class Statistic:
    __monitoring = Monitoring()
    __downtime: int = 0
    __overload: int = 0
    __completed: int = 0

    __MONITORING_DELAY = 100

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Statistic, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.update_stats())

    async def make_load(self, load_type: Load = Load.LOW):
        await self.__monitoring.fake_load(load_type)
        self.__completed += 1

    def clear_data(self):
        self.__downtime, self.__overload, self.__completed = 0, 0, 0

    def get_stats(self):
        old_downtime, old_overload, old_completed = self.__downtime, self.__overload, self.__completed
        self.clear_data()
        return old_downtime, old_overload, old_completed

    async def update_stats(self):
        while True:
            if self.__monitoring.working_process_count <= 0:
                self.__downtime += self.__MONITORING_DELAY
            if self.__monitoring.working_process_count > self.__monitoring.max_process_count:
                self.__overload += self.__MONITORING_DELAY
            await asyncio.sleep(self.__MONITORING_DELAY / 1000)
