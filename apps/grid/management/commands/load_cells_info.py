import argparse
import csv

from django.core.management.base import BaseCommand

from grid.models import Cell
from backend.settings import FEATURES


class Command(BaseCommand):
    help = 'Loads cell info'

    def add_arguments(self, parser):
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        file_data = kwargs['data']

        reader = csv.DictReader(file_data, delimiter=',')

        for row in reader:
            try:
                index = int(row['id'])
                info = ','.join([row[f] for f in FEATURES])
            except ValueError:
                print('Некорректные данные')
                return

            obj = Cell.objects.get(id=index)
            obj.info = info

            obj.save()
