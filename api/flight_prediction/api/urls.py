# mon_application/urls.py
from django.urls import path
from .views import home, Predict

urlpatterns = [
    path("", home, name="home"),
    path("api/predict/", Predict.as_view(), name="predict"),
]
