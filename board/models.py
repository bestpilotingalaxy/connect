from django.db import models
from profiles.models import UserProfile


class Platform(models.Model):
    name = models.CharField('Платформа', max_length=20)
    img = models.ImageField('Изображение', upload_to='platform', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'


class ContentType(models.Model):
    name = models.CharField('Тип контента', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип контента'
        verbose_name_plural = 'Тип контента'


class AdvertCategory(models.Model):
    name = models.CharField('Категория', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Advert(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    platform = models.ForeignKey(
        Platform,
        verbose_name='Платформа',
        on_delete=models.PROTECT
    )
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Тип контента',
        on_delete=models.PROTECT
    )
    advert_category = models.ForeignKey(
        AdvertCategory,
        verbose_name='Категория',
        on_delete=models.PROTECT
    )
    title = models.CharField('Заголовок', max_length=30, db_index=True)
    content = models.TextField('Описание', max_length=200)
    price = models.IntegerField('Цена',  null=True, blank=True)
    published = models.DateTimeField('Опубликовано', auto_now_add=True)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'


class Review(models.Model):
    advert = models.ForeignKey(
        Advert,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    text = models.TextField('Текст отзыва', max_length=1000)
    published = models.DateTimeField('Опубликовано', auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.advert}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['published']
