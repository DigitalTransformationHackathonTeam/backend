# LocationOptimization

Бэкенд для приложения поиска оптимального места для предприятия

## Установка пакетов

```shell
$ pip3 install -r requirements.txt
```

## Подготовка к работе

Применить миграции:

```shell
$ python3 manage.py migrate
```

Создать теги для бизнеса:

```shell
$ python3 manage.py create_tags datasets/business/business_tags.csv
```

Создать бизнесы:

```shell
$ python3 manage.py create_businesses
```

Создать город:

```shell
$ python3 manage.py create_grid Moscow datasets/business/business_tags.csv
```

```shell
$ python3 manage.py load_dist_to_underground Moscow datasets/grid/metro_distance.csv
```

```shell
$ python3 manage.py load_population Moscow datasets/grid/population.csv
```


## Запуск сервера

```shell
$ python3 manage.py runserver 0:8000
```

