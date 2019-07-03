from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.CurseListView.as_view()),
    path('create/', views.CurseCreateView.as_view()),

    # Curse info
    path('<int:pk>/', views.CurseDetailListView.as_view()),
    path('<int:pk>/lessons/', views.LessonListView.as_view()),

    # Lesson info
    path('lesson/<int:pk>/', views.LessonDetailListView.as_view()),
]
