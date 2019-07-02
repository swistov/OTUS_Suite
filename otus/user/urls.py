from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('reserved/<int:pk>/', views.ReservedUserCurseView.as_view(), name='reserved_curses')
]
