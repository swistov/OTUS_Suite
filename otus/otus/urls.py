from django.conf import settings
from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', trigger_error),
    path('admin/', admin.site.urls),
    path('admin/rq/', include('django_rq.urls')),
    path('api/v1.0/curse/', include('main.urls')),
    path('api/v1.0/user/', include('user.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
