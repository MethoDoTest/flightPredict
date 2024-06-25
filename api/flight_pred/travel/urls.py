from django.urls import path
from .views import travel_view

urlpatterns = [
    path('', travel_view, name='travel'),
]
