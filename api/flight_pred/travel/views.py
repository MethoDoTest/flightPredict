from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TravelForm
import requests


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

                api_url = "http://127.0.0.1:8000/travel/travel"
                data = {
                    "departure": departure,
                    "destination": destination,
                    "airline": airline,
                    "total_stops": total_stops,
                    "date": date,
                    "month": month,
                    "year": year,
                    "dep_hours": dep_hours,
                    "dep_min": dep_min,
                    "arrival_hours": arrival_hours,
                    "arrival_min": arrival_min,
                    "duration_hours": duration_hours,
                    "duration_min": duration_min,
                }
                try:
                    response = requests.post(
                        api_url, json=data, headers={"Content-Type": "application/json"}
                    )
                    response.raise_for_status()
                    if response.status_code == 200:
                        result = "result"
                    else:
                        result = "L'appel à l'API n'a pas réussi comme prévu."
                except requests.RequestException as e:
                    errors = f"Erreur lors de l'appel à l'API: {e}"
            else:
                errors = form.errors

            # Vérifiez si la requête demande une réponse JSON
            if request.headers.get("X-Requested-With") == "XMLHttpRequest":
                return JsonResponse({"result": result, "errors": errors})

        elif "clear" in request.POST:
            form = TravelForm()

    print(result)

    return render(
        request,
        "travel/travel_form.html",
        {"form": form, "result": result, "errors": errors},
    )
