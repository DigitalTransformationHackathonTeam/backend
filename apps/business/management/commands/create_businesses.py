from django.core.management.base import BaseCommand

from business.models import Business


sample_data = [
    {
        'business_name': 'Аптека',
        'eng_name': 'Pharmacy',
        'business_type': 'Goods',
        'weights': '2,1',
    },
    {
        'business_name': 'Парикмахерская',
        'eng_name': 'hair salon',
        'business_type': 'Service',
        'weights': '1, 2',
    },
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if Business.objects.all().exists():
            print('Уже созданы')
            return

        for obj in sample_data:
            Business.objects.create(**obj)
