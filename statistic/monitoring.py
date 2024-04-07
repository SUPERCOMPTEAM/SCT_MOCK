import datetime

class Monitoring:
    MAX_PROCESS_COUNT = 100
    current_process_count = 0

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Monitoring, cls).__new__(cls)
        return cls.instance

    def complete_process(self):
        self.current_process_count -= 1

    def start_process(self):
        self.current_process_count += 1
