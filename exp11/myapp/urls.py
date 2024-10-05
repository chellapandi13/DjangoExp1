# myapp/urls.py

from django.urls import path
from .views import welcome, about

urlpatterns = [
    path('', welcome, name='welcome'),  # This will be the welcome page
    path('about/', about, name='about'),  # This will be the about page
]
