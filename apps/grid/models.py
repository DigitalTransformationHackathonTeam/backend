from django.db import models
from django.db.models import CharField, ForeignKey, FloatField, IntegerField
import numpy as np


class Grid(models.Model):
    city_name = CharField('Название города', max_length=256, default='City')

    def __str__(self):
        return f'Сетка города {self.city_name}'


class Cell(models.Model):
    parent_grid = ForeignKey(Grid, related_name='cells',
                             verbose_name='Родительская сетка',
                             on_delete=models.CASCADE)

    latitude = FloatField('Широта левого верхнего угла', default=0.0)
    longitude = FloatField('Долгота левого верхнего угла', default=0.0)

    population = IntegerField('Население в данной ячейке', default=0)
    dist_to_underground = FloatField('Расстояние до ближайшей станции метро',
                                     default=0.0)

    def __str__(self):
        return f'Клетка ({self.latitude}, {self.longitude}) '\
               f'города {self.parent_grid.city_name}'

    def to_numpy(self):
        return np.array([self.population, self.dist_to_underground])
