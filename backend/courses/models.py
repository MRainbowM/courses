from basis.model_mixin import BaseTimestampedModel
from ckeditor.fields import RichTextField
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


class Chapter(BaseTimestampedModel):
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
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name='chapter',
        verbose_name='Раздел',
    )
    sort = models.IntegerField(verbose_name='Сортировка', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['sort']


class LessonItem(BaseTimestampedModel):
    lesson = models.ForeignKey(Lesson, models.CASCADE, 'lesson_items', verbose_name='Урок')
    text = RichTextField("Текст", default='', blank=True)
