from django.contrib import admin

from user.models import OtusUser, Teacher


@admin.register(OtusUser)
class OtusUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'last_name', 'first_name', 'phone')

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name')

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name
