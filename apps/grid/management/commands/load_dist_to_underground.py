import argparse
import csv

from django.core.management.base import BaseCommand

from grid.models import Grid, Cell


class Command(BaseCommand):
    help = 'Loads distance to underground'

    def add_arguments(self, parser):
        parser.add_argument('city', type=str, help='Город')
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        city = kwargs['city']
        file_data = kwargs['data']

        if not Grid.objects.filter(city_name=city).exists():
            print(f'Города {city} нет в базе')
            return

        reader = csv.DictReader(file_data, delimiter=',')

        for row in reader:
            try:
                index = int(row['id'])
                value = float(row['dist'])
            except ValueError:
                print('Некорректные данные')
                return

            obj = Cell.objects.get(id=index)
            obj.dist_to_underground = value

            obj.save()
