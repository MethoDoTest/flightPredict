from django.urls import path
from .views import travel_view, retrain_model_view, success_view

urlpatterns = [
    path("travel_view/", travel_view, name="travel_view"),
    path("retrain/", retrain_model_view, name="retrain_model_view"),
    path("success/", success_view, name="success_view"),
]
