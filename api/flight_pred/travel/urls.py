# urls.py
from django.urls import path
from .views import travel_view, retrain_model_view

urlpatterns = [
    path("travel/travel_view/", travel_view, name="travel_view"),
    path("travel/retrain/", retrain_model_view, name="retrain_model_view"),
]
