
from django.urls import path
from .views import destinations
urlpatterns = [
    path('dest',destinations),
]
