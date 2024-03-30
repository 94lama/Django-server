# from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='all_jobs'),
    path('my/', views.my_jobs, name='my_jobs'),
    path("detail/<int:id>/", views.job_detail),
    path("delete/<int:id>/", views.delete),
    path("edit/<int:id>/", views.edit),
]