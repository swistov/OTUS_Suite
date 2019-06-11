from django.urls import path

from app_main import views

app_name = 'app_main'

urlpatterns = [
    path('', views.index_app_main),
    path('api/curse/', views.CurseListView.as_view()),
    path('api/curse/<int:pk>', views.CurseDetailListView.as_view()),
]
