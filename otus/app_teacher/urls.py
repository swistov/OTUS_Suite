from django.urls import path

from app_teacher import views

app_name = 'app_teacher'

urlpatterns = [
    path('api/teacher/', views.TeacherListView.as_view()),
    path('api/teacher/<int:pk>', views.TeacherDetailListView.as_view()),
]
