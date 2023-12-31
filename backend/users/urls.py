from django.urls import path
from . import views

app_name = 'users'

urlpatterns=[
    path('', views.user, name='user'),
    path('register/', views.register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]