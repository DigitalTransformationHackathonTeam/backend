from django.core.management.base import BaseCommand

from business.models import BusinessCategory


sample_data = [
    {
        'category_name': 'Для пожилых',
        'eng_name': 'For elderly',
        'weights': '2,1',
    },
    {
        'category_name': 'Для молодых',
        'eng_name': 'For elderly',
        'weights': '2,1',
    },
    {
        'category_name': 'Для женщин',
        'eng_name': 'For women',
        'weights': '2,1',
    },
    {
        'category_name': 'Для мужчик',
        'eng_name': 'For men',
        'weights': '2,1',
    },
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if BusinessCategory.objects.all().exists():
            print('Уже созданы')
            return

        for obj in sample_data:
            BusinessCategory.objects.create(**obj)
