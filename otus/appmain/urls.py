from django.urls import path

from . import views

app_name = 'appmain'

urlpatterns = [
    path('', views.index_appmain),
    path('api/curse/', views.CurseListView.as_view()),
    path('api/curse/<int:pk>', views.CurseDetailListView.as_view()),
]
