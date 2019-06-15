from django.urls import path
from app_user import views

app_name = 'app_user'

urlpatterns = [
    path('api/create/', views.UserCreateView.as_view(), name='create'),
    path('api/login/', views.UserLoginView.as_view(), name='login'),
]
