from django.urls import path
from .views import password_validator

urlpatterns = [
    path('password_validator/', password_validator, name='password_validator'),
]
