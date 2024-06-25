from django.shortcuts import render
from .forms import TravelForm
import requests

def travel_view(request):
    result = None
    errors = None
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = TravelForm(request.POST)
            if form.is_valid():
                departure = form.cleaned_data['departure']
                destination = form.cleaned_data['destination']
                airline = form.cleaned_data['airline']
                total_stops = form.cleaned_data['total_stops']
                date = form.cleaned_data['date']
                month = form.cleaned_data['month']
                year = form.cleaned_data['year']
                dep_hours = form.cleaned_data['dep_hours']
                dep_min = form.cleaned_data['dep_min']
                arrival_hours = form.cleaned_data['arrival_hours']
                arrival_min = form.cleaned_data['arrival_min']
                duration_hours = form.cleaned_data['duration_hours']
                duration_min = form.cleaned_data['duration_min']

                "http://127.0.0.1:8000/travel/"  # remplacer par l'url de l'api !
                data = {
                    'departure': departure,
                    'destination': destination,
                    'airline': airline,
                    'total_stops': total_stops,
                    'date': date,
                    'month': month,
                    'year': year,
                    'dep_hours': dep_hours,
                    'dep_min': dep_min,
                    'arrival_hours': arrival_hours,
                    'arrival_min': arrival_min,
                    'duration_hours': duration_hours,
                    'duration_min': duration_min
                }
                try:
                    response = requests.post(api_url, json=data)
                    response.raise_for_status()
                    result = response.json().get('result', 'Aucun résultat trouvé')  # à modifier !
                except requests.RequestException as e:
                    errors = f"Erreur lors de l'appel à l'API: {e}"
            else:
                errors = form.errors
        elif 'clear' in request.POST:
            form = TravelForm()
    else:
        form = TravelForm()
    return render(request, 'travel/travel_form.html', {'form': form, 'result': result, 'errors': errors})



