from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index_app_main),
    path('all/', views.CurseListView.as_view()),
    path('<int:pk>/', views.CurseDetailListView.as_view()),
    path('<int:pk>/lessons/', views.LessonListView.as_view()),

    path('lesson/<int:pk>/', views.LessonDetailListView.as_view()),
]
