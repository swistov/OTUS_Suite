from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('api/create/', views.UserCreateView.as_view(), name='create'),
    path('api/login/', views.UserLoginView.as_view(), name='login'),
    path('api/reserved/<int:pk>/', views.ReservedUserCurseView.as_view(), name='reserved_curses')
]
