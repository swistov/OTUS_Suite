from django.urls import path

from teacher import views

app_name = 'teacher'

urlpatterns = [
    path('', views.TeacherListView.as_view()),
    path('<int:pk>/', views.TeacherDetailListView.as_view()),
]
