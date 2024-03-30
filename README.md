SCT Mock
=============
Мок-сервис для обучения модели и тестирования
----------------

### Подготовка
Установка зависимостей:
```sh
$  pip install -r requirements.txt  
```

Запуск проекта:
```sh
$  python main.py
```
------------------
### Конфигурирование

Для сервиса можно настроить три параметра: `api_host`, `api_port`, `server-number`. Их значения устанавливаются двумя способами:
Через аргументы командной строки:
- ```--api-host``` - хост/ip-адрес приложения. Дефолтное значение - `0.0.0.0`
- ```--api-port``` - порт подключения. Дефолтное значение - `8080`
- ```--server-number``` - номер сервера. Дефолтное значение - `1`
