from django.db import models
from django.db.models import CharField, ForeignKey, DecimalField


class Grid(models.Model):
    city_name = CharField('Название города', max_length=256, default='City')

    def __str__(self):
        return f'Сетка города {self.city_name}'


class Cell(models.Model):
    parent_grid = ForeignKey(Grid, related_name='cells',
                             verbose_name='Родительская сетка',
                             on_delete=models.CASCADE)

    latitude = DecimalField('Широта левого верхнего угла',
                            max_digits=8, decimal_places=6, default=0.0)
    longitude = DecimalField('Долгота левого верхнего угла',
                             max_digits=8, decimal_places=6, default=0.0)

    def __str__(self):
        return f'Клетка ({self.latitude}, {self.longitude})'\
               'города {self.parent_grid.city_name}'
