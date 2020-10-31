import numpy as np
from django.core.management.base import BaseCommand

from business.models import Business
from backend.settings import FEATURES


sample_data = [
    {
        'business_name': 'Аптека',
        'eng_name': 'Pharmacy',
        'business_type': 'Goods',
    },
    {
        'business_name': 'Парикмахерская',
        'eng_name': 'hair salon',
        'business_type': 'Service',
    },
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if Business.objects.all().exists():
            print('Уже созданы')
            return

        for obj in sample_data:
            weights = ','.join(
                [str(v) for v in np.random.random(len(FEATURES))]
            )
            Business.objects.create(**obj, weights=weights)
