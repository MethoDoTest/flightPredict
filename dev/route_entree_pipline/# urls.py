# urls.py
from django.urls import path
from .views import DataPipelineView

urlpatterns = [
    path('data-pipeline/', DataPipelineView.as_view(), name='data-pipeline'),
]
