SCT Mock
=============
Мок-сервис для обучения модели и тестирования
----------------

### Запуск
Сборка:
```sh
$   docker build -t mock  . 
```

Запуск проекта:
```sh
$  docker run -d --name mock -e MOCK_SERVER_NUMBER=5 -p 8080:8080 mock
```
------------------
### Конфигурирование

Для сервиса можно настроить четыре параметра: `api-host`, `api-port`, `server-number`, `max-process-count`. Их значения устанавливаются двумя способами:
#### Через аргументы командной строки:
- ```--api-host``` - хост/ip-адрес приложения. Дефолтное значение - `0.0.0.0`
- ```--api-port``` - порт подключения. Дефолтное значение - `8080`
- ```--server-number``` - номер сервера. Дефолтное значение - `1`
- ```--max-process-count``` - Максимальное число одновременно обрабатываемых потоков, если запросов больше числа потоков, то запрос лежит в очереди, и, следовательно, время его выполнения увеличивается. Дефолтное значение - `10`

#### Через установку переменных окружения
- ```MOCK_API_HOST``` - хост/ip-адрес приложения. Дефолтное значение - `0.0.0.0`
- ```MOCK_API_PORT``` - порт подключения. Дефолтное значение - `8080`
- ```MOCK_SERVER_NUMBER``` - номер сервера. Дефолтное значение - `1`
- ```MAX_PROCESS_COUNT``` - Дефолтное значение - `10`

-----------
### Сценарии использования

#### GET /hello
На данный запрос сервис вернёт в теле строку формата `hello from server N`, где N - установленный номер сервера

#### GET /load/random
Данный запрос будет эмулировать реальный запрос к серверу. `/random` означает, что время выполнения будет случайное, в диапозоне от 100 до 500 миллисекунд. Если запросов слишком много, время выполнения увеличивается.