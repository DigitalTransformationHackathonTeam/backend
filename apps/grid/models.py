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
    men = IntegerField('Процент мужчин', default=0)
    disabled = IntegerField('Процент инвалидов', default=0)
    elders = IntegerField('Процент пенсионеров', default=0)
    many_children = IntegerField('Процент из многодетных семей', default=0)
    young_parents = IntegerField('Процент молодых родителей', default=0)

    dist_to_underground = FloatField('Расстояние до ближайшей станции метро',
                                     default=0.0)
    underground_traffic = IntegerField('Количество людей, входящих в метро',
                                       default=0)

    cell_traffic = IntegerField('Количество людей, проходящих через клетку',
                                default=0)

    def __str__(self):
        return f'Клетка ({self.latitude}, {self.longitude}) '\
               f'города {self.parent_grid.city_name}'

    def to_numpy(self):
        return np.array(
                    self.population,
                    self.men,
                    self.disabled,
                    self.children,
                    self.elders,
                    self.many_children,
                    self.young_parents,
                    self.dist_to_underground,
                    self.underground_traffic,
                    self.cell_traffic,
               )
