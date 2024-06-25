# mon_application/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import FlightPredictionSerializer
from .forms import PredictionForm
import joblib

# Charger le modèle de machine learning
model = joblib.load("model.pkl")


class Predict(APIView):
    def post(self, request):
        serializer = FlightPredictionSerializer(data=request.data)
        if serializer.is_valid():
            input_data = serializer.validated_data["input_data"]
            prediction = model.predict([input_data])
            return Response(
                {"prediction": prediction.tolist()}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data["input_data"]
            prediction = model.predict([input_data])
            return render(request, "result.html", {"prediction": prediction})
    else:
        form = PredictionForm()
    return render(request, "index.html", {"form": form})
