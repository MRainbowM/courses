from django.contrib import admin

from .models import Course, Module, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort')
    fields = ('title',)
    list_per_page = 40
    empty_value_display = '-'
    search_fields = ('title',)
    sortable_by = ('title',)


@admin.register(Module)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'sort')
    fields = ('title', 'course', 'sort')
    list_per_page = 40
    empty_value_display = '-'
    list_filter = ('course',)
    search_fields = ('title',)
    sortable_by = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'sort')
    fields = ('title', 'chapter', 'text')
    list_per_page = 40
    empty_value_display = '-'
    list_filter = ('chapter',)
    search_fields = ('title',)
    sortable_by = ('title',)
