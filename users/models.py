from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email', help_text='введите адрес электронной почты')

    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE, help_text='загрузите свой аватар')
    phone = PhoneNumberField(verbose_name='телефон', **NULLABLE, help_text='введите номер телефона')
    country = CountryField(verbose_name='страна', **NULLABLE, help_text='выберите страну')

    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
