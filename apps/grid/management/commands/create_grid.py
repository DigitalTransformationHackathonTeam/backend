import argparse
import json
import os

import geojson
from django.core.management.base import BaseCommand

from grid.models import Grid, Cell
from backend.settings import GRID_STEP, GRID_START_LOC, GRID_END_LOC, BASE_DIR


class Command(BaseCommand):
    help = 'Creates grid for city'

    def add_arguments(self, parser):
        parser.add_argument('city', type=str, help='Город')
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        city = kwargs['city']
        file_data = kwargs['data']

        if Grid.objects.filter(city_name=city).exists():
            print(f'Город {city} уже есть в базе')
            return

        try:
            geojson.load(file_data)
        except json.decoder.JSONDecodeError:
            print(f'Файл {file_data.name} некорректен')
            return

        file_data.close()

        city_grid = Grid.objects.create(city_name=city)

        rows_cnt = int(abs(GRID_END_LOC[0] - GRID_START_LOC[0]) / GRID_STEP)
        cols_cnt = int(abs(GRID_END_LOC[1] - GRID_START_LOC[1]) / GRID_STEP)

        print(rows_cnt, cols_cnt, flush=True)

        output_dir = f'{BASE_DIR}/output'

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f'{output_dir}/result.csv', 'w') as out:
            lat = GRID_START_LOC[0]
            for i in range(rows_cnt):
                lon = GRID_START_LOC[1]
                for j in range(cols_cnt):
                    cell = Cell.objects.create(parent_grid=city_grid,
                                               latitude=lat, longitude=lon)

                    out.write(f"{cell.id},{lat},{lon}\n")
                    lon += GRID_STEP
                    # lon = round(lon + GRID_STEP, 6)
                lat -= GRID_STEP
                # lat = round(lat - GRID_STEP, 6)
