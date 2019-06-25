from django.urls import path

from teacher import views

app_name = 'teacher'

urlpatterns = [
    path('api/teacher/', views.TeacherListView.as_view()),
    path('api/teacher/<int:pk>', views.TeacherDetailListView.as_view()),
]
