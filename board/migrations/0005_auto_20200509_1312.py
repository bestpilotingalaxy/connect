# Generated by Django 3.0.6 on 2020-05-09 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20200506_1923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertcategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='contenttype',
            options={'verbose_name': 'Тип контента', 'verbose_name_plural': 'Тип контента'},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'verbose_name': 'Платформа', 'verbose_name_plural': 'Платформы'},
        ),
    ]