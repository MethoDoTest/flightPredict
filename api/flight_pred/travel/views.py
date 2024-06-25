from django.shortcuts import render
from .forms import TravelForm
import requests


def travel_view(request):
    result = None
    errors = None
    if request.method == "POST":
        if "submit" in request.POST:
            form = TravelForm(request.POST)
            if form.is_valid():
                departure = form.cleaned_data["departure"]
                destination = form.cleaned_data["destination"]

                api_url = (
                    "http://127.0.0.1:8000/travel/"  # remplacer par l'url de l'api !
                )
                data = {"departure": departure, "destination": destination}
                try:
                    response = requests.post(api_url, json=data)
                    response.raise_for_status()
                    result = response.json().get(
                        "result", "Aucun résultat trouvé"
                    )  # à modifier !
                except requests.RequestException as e:
                    errors = f"Erreur lors de l'appel à l'API: {e}"
            else:
                errors = form.errors
        elif "clear" in request.POST:
            form = TravelForm()
    else:
        form = TravelForm()
    return render(
        request,
        "travel/travel_form.html",
        {"form": form, "result": result, "errors": errors},
    )
