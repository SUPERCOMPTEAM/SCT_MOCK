from aiohttp import web
from configargparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from api.load_handler import LoadHandler
from api.stupid_handler import StupidHandler
from api.stats_handler import StatsHandler
from statistic.monitoring import Monitoring

# Номер сервера
server_number = 1

# Парсинг аргументов
parser = ArgumentParser(
    auto_env_var_prefix='MOCK_',
    formatter_class=ArgumentDefaultsHelpFormatter
)
parser.add_argument('--api-host', default='0.0.0.0',
                    help='IPv4/IPv6 address API server would listen on')
parser.add_argument('--api-port', type=int, default=8080,
                    help='TCP port API server would listen on')
parser.add_argument('--server-number', type=int, default=1,
                    help='Server number')
parser.add_argument('--max-process-count', type=int, default=10,
                    help='Maximum number of concurrent requests')
args = parser.parse_args()
server_number = args.server_number

# Задание параметров фейковой нагрузки
Monitoring(args.max_process_count)

# Энд-поинты
app = web.Application()
stupid = StupidHandler(server_number)
stats = StatsHandler()
load = LoadHandler(server_number)
app.router.add_route('GET', '/hello', stupid.hello)
app.router.add_route('GET', '/stats/now', stats.get_current_stats)
app.router.add_route('GET', '/load/random', load.load_random)

web.run_app(app, host=args.api_host, port=args.api_port)
