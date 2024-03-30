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

Для сервиса можно настроить три параметра: `api_host`, `api_port`, `server-number`. Их значения устанавливаются двумя способами:
#### Через аргументы командной строки:
- ```--api-host``` - хост/ip-адрес приложения. Дефолтное значение - `0.0.0.0`
- ```--api-port``` - порт подключения. Дефолтное значение - `8080`
- ```--server-number``` - номер сервера. Дефолтное значение - `1`

#### Через установку переменных окружения
- ```MOCK_API_HOST``` - хост/ip-адрес приложения. Дефолтное значение - `0.0.0.0`
- ```MOCK_API_PORT``` - порт подключения. Дефолтное значение - `8080`
- ```MOCK_SERVER_NUMBER``` - номер сервера. Дефолтное значение - `1`

-----------
### Сценарии использования

#### GET /hello
На данный запрос сервис вернёт в теле строку формата `hello from server N`, где N - установленный номер сервера