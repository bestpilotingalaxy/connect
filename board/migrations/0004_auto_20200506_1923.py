# Generated by Django 3.0.6 on 2020-05-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200506_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertcategory',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Тип контента'),
        ),
        migrations.AlterField(
            model_name='platform',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Платформа'),
        ),
    ]