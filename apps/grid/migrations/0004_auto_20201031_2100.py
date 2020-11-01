# Generated by Django 3.1.2 on 2020-10-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid', '0003_auto_20201031_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='cell_traffic',
            field=models.IntegerField(default=0, verbose_name='Количество людей, проходящих через клетку'),
        ),
        migrations.AddField(
            model_name='cell',
            name='disabled',
            field=models.IntegerField(default=0, verbose_name='Процент инвалидов'),
        ),
        migrations.AddField(
            model_name='cell',
            name='elders',
            field=models.IntegerField(default=0, verbose_name='Процент пенсионеров'),
        ),
        migrations.AddField(
            model_name='cell',
            name='many_children',
            field=models.IntegerField(default=0, verbose_name='Процент из многодетных семей'),
        ),
        migrations.AddField(
            model_name='cell',
            name='men',
            field=models.IntegerField(default=0, verbose_name='Процент мужчин'),
        ),
        migrations.AddField(
            model_name='cell',
            name='underground_traffic',
            field=models.IntegerField(default=0, verbose_name='Количество людей, входящих в метро'),
        ),
        migrations.AddField(
            model_name='cell',
            name='young_parents',
            field=models.IntegerField(default=0, verbose_name='Процент молодых родителей'),
        ),
    ]
