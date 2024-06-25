from django.shortcuts import render
from .forms import TravelForm

def travel_view(request):
    result = None
    errors = None
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = TravelForm(request.POST)
            if form.is_valid():
                departure = form.cleaned_data['departure']
                destination = form.cleaned_data['destination']
                result = 'result' # affichage du résultat prédit 
            else:
                errors = form.errors
        elif 'clear' in request.POST:
            form = TravelForm()
    else:
        form = TravelForm()
    return render(request, 'travel/travel_form.html', {'form': form, 'result': result, 'errors': errors})
