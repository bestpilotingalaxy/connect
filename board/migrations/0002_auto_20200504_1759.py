# Generated by Django 3.0.6 on 2020-05-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name': 'Обьявления', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.RenameField(
            model_name='advert',
            old_name='date',
            new_name='published',
        ),
    ]
