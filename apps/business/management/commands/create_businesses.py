from django.core.management.base import BaseCommand

from business.models import Business


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if Business.objects.all().exists():
            print('Уже созданы')
            return

        Business.objects.create(business_name='Парикмахерская')
        Business.objects.create(business_name='Аптека')
        Business.objects.create(business_name='Продуктовый магазин')
