from django.contrib import admin

from main.models import Curse, Lesson


@admin.register(Curse)
class CurseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'descriptions', 'enabled'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'curse', 'date_time_release', 'enabled', 'add_date'
