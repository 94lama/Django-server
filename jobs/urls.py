# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my/', views.my_jobs, name='my_jobs'),
]
