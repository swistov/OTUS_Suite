from django.contrib import admin

from user.models import ReservedCurse, OtusUser


@admin.register(ReservedCurse)
class ReservedCurseAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'curse', 'reserved_date_time'


@admin.register(OtusUser)
class OtusUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'last_name', 'first_name', 'phone')

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name
