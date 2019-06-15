from django.contrib import admin

from app_user.models import ReservedCurse


@admin.register(ReservedCurse)
class ReservedCurseAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'curse', 'reserved_date_time'
