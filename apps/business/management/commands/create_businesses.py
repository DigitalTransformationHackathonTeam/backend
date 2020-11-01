import csv
import argparse

import numpy as np
from django.core.management.base import BaseCommand

from business.models import Business
from backend.settings import FEATURES


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        if Business.objects.all().exists():
            print('Уже созданы')
            return

        file_data = kwargs['data']

        reader = csv.DictReader(file_data, delimiter=',')

        for row in reader:
            props = dict()
            props['business_name'] = row['business_name']
            props['eng_name'] = row['eng_name']
            props['business_type'] = row['business_type']
            props['weights'] = ','.join([
                str(v) for v in np.random.random(len(FEATURES))
            ])

            Business.objects.create(**props)
