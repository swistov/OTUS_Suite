from django.contrib import admin

from user.models import ReservedCurse, OtusUser, Teacher


@admin.register(ReservedCurse)
class ReservedCurseAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'get_curses_str', 'reserved_date_time'

    def get_curses_str(self, obj):
        return ' '.join(obj.curse.all().values_list("name", flat=True))
    get_curses_str.short_description = 'Curses'


@admin.register(OtusUser)
class OtusUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'last_name', 'first_name', 'phone')

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'first_name'

    search_fields = ["user__first_name"]
