# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:job_id>/", views.job, name="job"),
    path("<str:key>=<str:value>", views.search_job, name="jobs"),
]
