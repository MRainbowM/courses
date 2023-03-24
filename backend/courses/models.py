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
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['sort']


class Lesson(BaseTimestampedModel):
    title = models.CharField('Название', max_length=256)
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='module',
        verbose_name='Раздел',
    )
    sort = models.IntegerField(verbose_name='Сортировка', null=True)
    text = CKEditor5Field('Текст', default='', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['sort']
