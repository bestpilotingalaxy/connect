from django.db import models


# Create your models here.


class Platform(models.Model):
    name = models.CharField('Платформа', max_length=20)

    def __str__(self):
        return self.name


class ContentType(models.Model):
    name = models.CharField('Тип контента', max_length=50)

    def __str__(self):
        return self.name


class AdvertCategory(models.Model):
    name = models.CharField('Категория', max_length=20)

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField('Заголовок', max_length=30, db_index=True)
    content = models.TextField('Описание', max_length=200)
    price = models.FloatField('Цена', null=True, blank=True)
    published = models.DateTimeField('Опубликовано', auto_now_add=True)
    platform = models.ForeignKey(
        Platform, verbose_name='Платформа', on_delete=models.PROTECT
    )
    content_type = models.ForeignKey(
        ContentType, verbose_name='Тип контента', on_delete=models.PROTECT
    )
    advert_category = models.ForeignKey(
        AdvertCategory, verbose_name='Категория', on_delete=models.PROTECT
    )

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
