from django.contrib.auth.models import User
from django.db import models

from courses.models import Course


class Client(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_client',
        verbose_name='Пользователь',
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name='Активность',
        help_text='Включено - участвует в проекте, выключено - нет',
        default=True,
    )

    def __str__(self):
        name = ''
        if self.user.first_name is not None:
            name += self.user.first_name

        if self.user.last_name is not None:
            name += self.user.last_name

        if name == '':
            name = self.user.username

        return name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class ClientCourse(models.Model):
    """Курсы участника"""
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='client_course',
        verbose_name='Клиент'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='client_course',
        verbose_name='Курс'
    )
    active = models.BooleanField(
        verbose_name='Активность',
        help_text='Включено - есть доступ к курсу, выключено - нет',
        default=False,
    )


class ClientLesson(models.Model):
    """Пройденные уроки участника"""
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='client_lesson',
        verbose_name='Клиент'
    )
    lesson = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='client_lesson',
        verbose_name='Урок'
    )
    completed = models.BooleanField(
        verbose_name='Выполнен',
        help_text='Включено - урок пройден, выключено - нет',
        default=False,
    )
