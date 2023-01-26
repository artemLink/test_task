from django.contrib import admin
from django.urls import path, include
from . import views
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main, name = 'main_page'),
    path('register/', register, name = 'register'),
    path('user_login/', auth_views.LoginView.as_view(template_name = './user_login.html'), name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),

]