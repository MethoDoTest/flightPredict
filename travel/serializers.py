from rest_framework import serializers
from .models import FlightPredictionModel


class FlightPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightPredictionModel
        fields = "__all__"
