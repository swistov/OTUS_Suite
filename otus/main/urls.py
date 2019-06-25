from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index_app_main),
    path('api/curses/', views.CurseListView.as_view()),
    path('api/curse/<int:pk>/', views.CurseDetailListView.as_view()),
    path('api/curse/<int:pk>/lessons/', views.LessonListView.as_view()),
    path('api/lesson/<int:pk>/', views.LessonDetailListView.as_view()),
]
