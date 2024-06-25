from django.shortcuts import render
from .forms import TravelForm

def travel_view(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            departure = form.cleaned_data['departure']
            destination = form.cleaned_data['destination']
            # traitement des données
    else:
        form = TravelForm()
    return render(request, 'travel/travel_form.html', {'form': form})
