# from django.contrib import admin
from django.urls import path, include
from .views import TestView
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify

urlpatterns = [
    path('', TestView.as_view(), name='index'),
    path('token/', token_obtain_pair, name='token_obtain_pair'),
    path('refresh/', token_refresh, name='token_refresh'),
    path('login/', token_verify, name='token_verify'),
]