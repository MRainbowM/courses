from django.contrib import admin
from .models import Course, Chapter, Lesson, LessonItem


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort')
    fields = ('title',)
    list_per_page = 40
    empty_value_display = '-'
    search_fields = ('title',)
    sortable_by = ('title',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'sort')
    fields = ('title', 'course')
    list_per_page = 40
    empty_value_display = '-'
    list_filter = ('course',)
    search_fields = ('title',)
    sortable_by = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'sort')
    fields = ('title', 'chapter')
    list_per_page = 40
    empty_value_display = '-'
    list_filter = ('chapter',)
    search_fields = ('title',)
    sortable_by = ('title',)


@admin.register(LessonItem)
class LessonItemAdmin(admin.ModelAdmin):
    list_display = ('lesson',)
    fields = ('lesson', 'text')
    list_per_page = 40
    empty_value_display = '-'

    search_fields = ('lesson',)
    sortable_by = ('lesson',)
