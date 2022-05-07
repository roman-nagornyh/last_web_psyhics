from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Account(AbstractUser):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

#
# class Psychic(models.Model):
#     user = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name='Учетная запись')
#     level_authenticity = models.FloatField(verbose_name='Уровень достоверности', null=False,
#                                            default=100.0, blank=True)
#
#     class Meta:
#         manage = False
#
#
# class HistoryUser(models.Model):
#     user = models.ForeignKey(Account, null=False, on_delete=models.CASCADE, verbose_name='Пользователь')
#     value = models.IntegerField(null=False, verbose_name='Загаданное значение')
#     send_date = models.DateTimeField(null=False, auto_now_add=True, verbose_name='Время отправки')
#
#     class Meta:
#         manage = False
#
#
# class PsychicHistory(models.Model):
#     psychic = models.ForeignKey(Account, null=False, verbose_name='Экстрасенс', on_delete=models)
#     is_success = models.BooleanField(null=False, blank=False, verbose_name='Результат')
#     intended_value = models.IntegerField(null=False, blank=False)
#
#     class Meta:
#         manage = False