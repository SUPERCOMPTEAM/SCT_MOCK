import asyncio

from enum import Enum


class Load(Enum):
    LOW = 100
    MIDDLE = 300
    HIGH = 500


class Monitoring:
    _working_process_count = 0
    _queue_process_count = 0
    _max_process_count = 100

    def __new__(cls, max_process=100):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Monitoring, cls).__new__(cls)
        return cls.instance

    def __init__(self, max_process=100):
        self._max_process_count = max_process

    async def fake_load(self, load_type: Load):
        # Кладём в очередь
        self._queue_process_count += 1
        # Ожидание выполнения в очереди
        while self.working_process_count >= self.max_process_count:
            await asyncio.sleep(0.01)
        #уходим из очереди
        self._queue_process_count -= 1
        self.start_process()
        await asyncio.sleep(load_type.value / 1000)
        self.complete_process()
        print("Complete process")

    def complete_process(self):
        self._working_process_count -= 1

    def start_process(self):
        self._working_process_count += 1

    @property
    def max_process_count(self):
        return self._max_process_count

    @property
    def working_process_count(self):
        return self._working_process_count
