from statistic.monitoring import Monitoring
import asyncio

class Statistic:

    monitoring = Monitoring()
    downtime = 0
    overload = 0
    completed = 0

    MONITORING_DELAY = 100

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Statistic, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.update_stats())


    def start_process(self):
        self.monitoring.start_process()

    def end_process(self):
        self.monitoring.complete_process()
        self.completed += 1


    async def update_stats(self):
        while True:
            if self.monitoring.current_process_count <= 0:
                self.downtime += self.MONITORING_DELAY
            if self.monitoring.current_process_count > self.monitoring.MAX_PROCESS_COUNT:
                self.overload += self.MONITORING_DELAY
            await asyncio.sleep(self.MONITORING_DELAY / 1000)