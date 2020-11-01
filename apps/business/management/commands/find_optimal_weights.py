import argparse

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
import pandas as pd
from django.core.management.base import BaseCommand

from business.models import Business


def find_weights_for_business_type(X, y):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    model = Ridge()
    model.fit(X_scaled, y)
    weights = model.coef_
    return weights


class Command(BaseCommand):
    help = 'Finds optimal weights for business'

    def add_arguments(self, parser):
        parser.add_argument('data', type=argparse.FileType('r'),
                            help='Файл с данными')

    def handle(self, *args, **kwargs):
        file_data = kwargs['data']

        df = pd.read_csv(file_data)

        for business_name in df['business_name'].unique():
            X = df[df.business_name == business_name].drop(columns={
                                                            'success',
                                                            'business_name',
                                                            'business_type',
                                                            'eng_name',
                                                           })
            y = df[df.business_name == business_name]['success']

            weights = find_weights_for_business_type(X, y)
            weights_str = ','.join([str(v) for v in weights])

            obj = Business.objects.get(business_name=business_name)
            obj.weights = weights_str
            obj.save()
