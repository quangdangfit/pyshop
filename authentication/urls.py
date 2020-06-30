# coding=utf-8
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import Register


urlpatterns = [
    path('/users', Register.as_view()),
    path('/login', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
]
