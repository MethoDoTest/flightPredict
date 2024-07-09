# views.py
from django.http import JsonResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import subprocess
from .forms import TravelForm
from .prediction_model import (
    load_model,
    predict_flight_price,
)  # Importer votre modèle de prédiction


@csrf_exempt
def travel_view(request):
    result = None
    errors = None
    form = TravelForm()

    if request.method == "POST":
        if "submit" in request.POST:
            form = TravelForm(request.POST)
            if form.is_valid():
                departure = form.cleaned_data["departure"]
                destination = form.cleaned_data["destination"]
                airline = form.cleaned_data["airline"]
                total_stops = form.cleaned_data["total_stops"]
                date = form.cleaned_data["date"]
                month = form.cleaned_data["month"]
                year = form.cleaned_data["year"]
                dep_hours = form.cleaned_data["dep_hours"]
                dep_min = form.cleaned_data["dep_min"]
                arrival_hours = form.cleaned_data["arrival_hours"]
                arrival_min = form.cleaned_data["arrival_min"]
                duration_hours = form.cleaned_data["duration_hours"]
                duration_min = form.cleaned_data["duration_min"]

                # Charger le modèle
                model = load_model()

                # Appel de la fonction de prédiction avec les données du formulaire
                try:
                    result = predict_flight_price(
                        model,
                        departure,
                        destination,
                        airline,
                        total_stops,
                        date,
                        month,
                        year,
                        dep_hours,
                        dep_min,
                        arrival_hours,
                        arrival_min,
                        duration_hours,
                        duration_min,
                    )
                except Exception as e:
                    errors = f"Erreur lors de la prédiction: {e}"
            else:
                errors = form.errors

            print("Result:", result)
            print("Errors:", errors)

            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({"result": result, "errors": errors})

        elif "clear" in request.POST:
            form = TravelForm()

    return render(
        request,
        "travel/travel_form.html",
        {"form": form, "result": result, "errors": errors},
    )


def retrain_model_view(request):
    if request.method == "POST" and "csv_file" in request.FILES:
        csv_file = request.FILES["csv_file"]
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.url(filename)
        file_path = os.path.join(fs.location, filename)
        subprocess.call(["python", "travel/../../../train/train.py", file_path])
        return redirect("success_view")
    return render(request, "travel/retrain_model.html")


def success_view(request):
    return render(request, "travel/success.html")
