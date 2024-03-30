from aiohttp import web
from configargparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from api.stupid import Stupid

# Номер сервера
server_number = 1

# Парсинг аргументов
parser = ArgumentParser(
    auto_env_var_prefix='MOCK_',
    formatter_class=ArgumentDefaultsHelpFormatter
)
parser.add_argument('--api-address', default='0.0.0.0',
                    help='IPv4/IPv6 address API server would listen on')
parser.add_argument('--api-port', type=int, default=8080,
                    help='TCP port API server would listen on')
parser.add_argument('--server-number', type=int, default=1,
                    help='Server number')
args = parser.parse_args()
server_number = args.server_number

# Энд-поинты
app = web.Application()
stupid = Stupid(server_number)
app.router.add_route('GET', '/hello', stupid.hello)

web.run_app(app, host=args.api_address, port=args.api_port)
