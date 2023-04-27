from basis.model_mixin import BaseTimestampedModel
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models


class Course(BaseTimestampedModel):
    title = models.CharField('Название', max_length=256)
    sort = models.IntegerField(verbose_name='Сортировка', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['sort']


class Module(BaseTimestampedModel):
    title = models.CharField('Название', max_length=256)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course',
        verbose_name='Курс',
    )
    sort = models.IntegerField(verbose_name='Сортировка', null=True)

    def __str__(self):
        return f'{self.course.title} - {self.title}'

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['sort']


class Lesson(BaseTimestampedModel):
    title = models.CharField('Название', max_length=256)
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='module',
        verbose_name='Модуль',
    )
    sort = models.IntegerField(verbose_name='Сортировка', null=False, blank=False)
    text = CKEditor5Field('Текст', default='', blank=True)
    video_url = models.URLField('Видео URL', blank=True)
    
    def __str__(self):
        return f'{self.title} ({self.module.course.title} - {self.module.title})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['sort']
