from django.db import models
from django.db.models import CharField

import numpy as np


class Business(models.Model):
    GOODS = 'Goods'
    SERVICE = 'Service'

    BUSINESS_TYPE_CHOICES = [
        (GOODS, 'Товары'),
        (SERVICE, 'Услуги'),
    ]

    business_name = CharField('Название бизнеса', max_length=1024, default='')
    eng_name = CharField('Название на английском', max_length=1024, default='')
    weights = CharField('Веса в формате csv', max_length=1024, default='0.0')
    business_type = CharField('Тип бизнеса', max_length=10,
                              choices=BUSINESS_TYPE_CHOICES, default=GOODS)

    def to_numpy(self):
        return np.array([float(w) for w in self.weights.split(',')])

    def __str__(self):
        return f'Модель бизнеса {self.business_name}'

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.lower()
        self.eng_name = '_'.join(self.eng_name.split(' '))
        super(Business, self).save(*args, **kwargs)

# class BusinessCategory:
#     def __init__(self, type_name: str):
#         self.type = type_name
#         self.weight = np.array([])

#         # Load weights vector for this business type
#         self.load_weights()

#     def load_weights(self):
#         with open('category_factor_weights.csv') as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=',')
#             factors = next(csv_reader)[1:]
#             for row in csv_reader:
#                 if row[0] == self.type:
#                     self.weight = np.array(list(map(int, row[1:])))
