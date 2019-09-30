import requests

from django.contrib import admin
from django.db.models import Prefetch

from main.models import Curse, Lesson, CurrencyRate
from user.models import Teacher


@admin.register(Curse)
class CurseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_teachers_str', 'descriptions', 'enabled')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        prefetch_qs = Teacher.objects.only('user')
        prefetch = Prefetch(
            'teachers',
            queryset=prefetch_qs
        )
        qs = qs.prefetch_related(prefetch)
        return qs

    def get_teachers_str(self, obj):
        return ' '.join(obj.teachers.values_list("user__last_name", flat=True))
    get_teachers_str.short_description = 'Teachers'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'curse', 'teacher', 'date_time_release', 'enabled', 'add_date')


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    actions = ['update_currency_rates', ]

    def update_currency_rates(self, request, queryset):

        for rate in queryset:
            pair = '{}RUB'.format(rate.currency.upper())
            try:
                response = requests.get(
                    'https://www.freeforexapi.com/api/live?pairs={}'.format(pair)
                )
            except ConnectionError as e:
                return 'Bad request. Error: {}'.format(e)

            data = response.json()
            rate.rate = data['rates'][pair]['rate']
            rate.save(update_fields=['rate'])
