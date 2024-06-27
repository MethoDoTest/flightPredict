from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TravelForm
import requests


@csrf_exempt
def travel_view(request):
    result = None
    errors = None
    form = TravelForm()  # Assurez-vous que form est toujours défini

    if request.method == "POST":
        if "submit" in request.POST:
            form = TravelForm(request.POST)
            if form.is_valid():
                departure = form.cleaned_data["departure"]
                destination = form.cleaned_data["destination"]

                api_url = (
                    "http://127.0.0.1:8000/travel/"  # Remplacer par l'URL de l'API !
                )
                data = {"departure": departure, "destination": destination}
                try:
                    response = requests.post(api_url, json=data)
                    response.raise_for_status()
                    result = response.json().get(
                        "result", "Aucun résultat trouvé"
                    )  # À modifier selon la réponse de votre API
                except requests.RequestException as e:
                    errors = f"Erreur lors de l'appel à l'API: {e}"
            else:
                errors = form.errors
        elif "clear" in request.POST:
            form = TravelForm()

    return render(
        request,
        "travel/travel_form.html",
        {"form": form, "result": result, "errors": errors},
    )
