from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
     path('', views.login, name='login'),
     path('register/', views.register, name='register'),
     path('home/<str:em>', views.home, name='home'),
     path('formdata/', views.formdata, name='formdata'),
     path('datadisplay/', views.datadisplay, name='datadisplay'),
     path('delete/<int:pk><str:em>', views.delete, name='delete'),
     path('edit/<int:pk>', views.edit, name='edit'),
     path('save/<int:pk>', views.save, name='save'),
     path('showdata/<str:em>',views.showdata,name='showdata'),
]