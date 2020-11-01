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
$ python3 manage.py create_businesses datasets/business/business_list.csv
```

Создать город:

```shell
$ python3 manage.py create_grid Moscow datasets/grid/mo.geojson
```

Загрузить данные в ячейки

```shell
$ python3 manage.py load_cells_info datasets/grid/FinalCellDate.csv
```

Найти оптимальные веса для бизнеса

```shell
$ python3 manage.py find_optimal_weights datasets/business/business_data.csv
```


## Запуск сервера

```shell
$ python3 manage.py runserver 0:8000
```

