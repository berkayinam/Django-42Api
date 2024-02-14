# urls.py
from django.urls import path
from .views import campus_users_view

urlpatterns = [
    path('', campus_users_view, name='campus-users'),
]