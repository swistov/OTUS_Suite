from django.contrib import admin

from django.contrib.auth.models import User

from app_teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'first_name'

    search_fields = ["user__first_name"]




