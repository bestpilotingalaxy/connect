# Generated by Django 3.0.6 on 2020-05-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20200522_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]