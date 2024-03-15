from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('check-email/', views.check_email, name='check-email'),
    # Add more URL patterns as needed
]
