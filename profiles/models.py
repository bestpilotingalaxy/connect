from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    username = models.CharField("Отображаемое имя", max_length=12)
    avatar = models.ImageField('Аватар', upload_to='profile/')
    first_name = models.CharField('Имя', max_length=50, blank=True, null=True)
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=True,
        null=True
    )
    social_link = models.URLField(
        'Информация для связи',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
