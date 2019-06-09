from django.contrib import admin

from .models import Curse


@admin.register(Curse)
class CurseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'descriptions', 'enabled'
