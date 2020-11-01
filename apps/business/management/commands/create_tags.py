import argparse
import csv

from django.core.management.base import BaseCommand

from business.models import BusinessTag
from backend.settings import FEATURES


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        file_data = kwargs['data']
        reader = csv.DictReader(file_data, delimiter=',')

        for row in reader:
            props = dict()
            props['tag_name'] = row['tag_name']
            props['eng_name'] = row['eng_name']
            props['weights'] = ','.join([row[f] for f in FEATURES])
            BusinessTag.objects.create(**props)
