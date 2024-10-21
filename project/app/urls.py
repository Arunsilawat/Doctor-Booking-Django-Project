from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
     path('', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('home/', views.home, name='home'),
     path('formdata/', views.formdata, name='formdata'),
     path('datadisplay/', views.datadisplay, name='datadisplay'),
]