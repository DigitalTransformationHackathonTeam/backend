# Generated by Django 3.1.2 on 2020-10-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0002_auto_20201030_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=8, verbose_name='Широта левого верхнего угла'),
        ),
        migrations.AddField(
            model_name='cell',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=8, verbose_name='Долгота левого верхнего угла'),
        ),
    ]
