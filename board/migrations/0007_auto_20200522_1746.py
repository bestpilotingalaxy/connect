# Generated by Django 3.0.6 on 2020-05-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_platform_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True, verbose_name='Цена'),
        ),
    ]
