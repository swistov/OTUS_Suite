from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('<int:pk>/', views.UserInfoView.as_view(), name='user_info'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name='login'),

    path('teacher/', views.TeacherListView.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetailListView.as_view()),
]
