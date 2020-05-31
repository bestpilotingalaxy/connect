from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class UserProfile(User):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='profile',
        parent_link=True
    )
    MESSENGER_CHOICES = [
        ('media/messengers/telegram-app.png', 'Telegram'),
        ('media/messengers/viber.png', 'Viber'),
        ('media/messengers/whatsapp.png', 'Whatsapp')
    ]
    messenger = models.CharField(
        'Мессенджер',
        max_length=250,
        choices=MESSENGER_CHOICES,
        blank=True,
        null=True
    )
    nickname = models.CharField('Отображаемое имя', max_length=16)
    avatar = models.ImageField('Аватар', upload_to='profile/')
    about = models.TextField('О себе', max_length=250, blank=True, null=True)
    contact_phone = PhoneField('Телефон для связи', blank=True, null=True)
    contact_link = models.URLField('Ссылка для связи', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
