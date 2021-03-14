from django.contrib import admin
from django.urls import path 
from django.contrib.auth import views
from .views import *
from accounts import views as users_views

app_name = "accounts"


urlpatterns = [
   path('login/', views.LoginView.as_view(), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   path('register/', users_views.register, name='register'),

]