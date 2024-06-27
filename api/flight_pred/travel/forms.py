# forms.py
from django import forms
import re
from .validation import (
    validate_airline,
    validate_source_destination,
    validate_total_stops,
    validate_price, # a utiliser pour le résultat
    validate_date,
    validate_time,
    validate_duration
)

class TravelForm(forms.Form):
    departure = forms.CharField(label='depart', max_length=100, required=True)
    destination = forms.CharField(label='destination', max_length=100, required=True)
    airline = forms.CharField(label='airline', max_length=100, required=True)
    total_stops = forms.IntegerField(label='total_stops', required=True)
    date = forms.IntegerField(label='date', required=True)
    month = forms.IntegerField(label='month', required=True)
    year = forms.IntegerField(label='year', required=True)
    dep_hours = forms.IntegerField(label='dep_hours', required=True)
    dep_min = forms.IntegerField(label='dep_min', required=True)
    arrival_hours = forms.IntegerField(label='arrival_hours', required=True)
    arrival_min = forms.IntegerField(label='arrival_min', required=True)
    duration_hours = forms.IntegerField(label='duration_hours', required=True)
    duration_min = forms.IntegerField(label='duration_min', required=True)

    def clean_departure(self):
        departure = self.cleaned_data['departure']
        if not re.match("^[A-Za-z\s]*$", departure):
            raise forms.ValidationError('le champ "depart" ne doit contenir que des lettres et des espaces !')
        return departure

    def clean_destination(self):
        destination = self.cleaned_data['destination']
        if not re.match("^[A-Za-z\s]*$", destination):
            raise forms.ValidationError('le champ "destination" ne doit contenir que des lettres et des espaces !')
        return destination

    def clean_airline(self):
        airline = self.cleaned_data['airline']
        if not re.match("^[A-Za-z\s]*$", airline):
            raise forms.ValidationError('le champ "airline" ne doit contenir que des lettres et des espaces !')
        if not validate_airline(airline):
            raise forms.ValidationError('Airline invalide.')
        return airline

    def clean_total_stops(self):
        total_stops = self.cleaned_data['total_stops']
        if not isinstance(total_stops, int):
            raise forms.ValidationError('le champ "total_stops" ne doit contenir qu\'un nombre !')
        if not validate_total_stops(total_stops):
            raise forms.ValidationError('Total stops invalide.')
        return total_stops

    def clean_date(self):
        date = self.cleaned_data['date']
        month = self.cleaned_data.get('month')
        year = self.cleaned_data.get('year')
        if not (1 <= date <= 31):
            raise forms.ValidationError('le champ "date" doit être un nombre entre 1 et 31 !')
        if month and year and not validate_date(date, month, year):
            raise forms.ValidationError('Date invalide.')
        return date

    def clean_month(self):
        month = self.cleaned_data['month']
        if not (1 <= month <= 12):
            raise forms.ValidationError('le champ "month" doit être un nombre entre 1 et 12 !')
        return month

    def clean_year(self):
        year = self.cleaned_data['year']
        if not (2000 < year < 2100):
            raise forms.ValidationError('le champ "year" doit être un nombre entre 2001 et 2099 !')
        return year

    def clean_dep_hours(self):
        dep_hours = self.cleaned_data['dep_hours']
        if not (0 <= dep_hours < 24):
            raise forms.ValidationError('le champ "dep_hours" doit être un nombre entre 0 et 24 !')
        return dep_hours

    def clean_dep_min(self):
        dep_min = self.cleaned_data['dep_min']
        if not (0 <= dep_min < 60):
            raise forms.ValidationError('le champ "dep_min" doit être un nombre entre 0 et 60 !')
        return dep_min

    def clean_arrival_hours(self):
        arrival_hours = self.cleaned_data['arrival_hours']
        if not (0 <= arrival_hours < 24):
            raise forms.ValidationError('le champ "arrival_hours" doit être un nombre entre 0 et 24 !')
        return arrival_hours

    def clean_arrival_min(self):
        arrival_min = self.cleaned_data['arrival_min']
        if not (0 <= arrival_min < 60):
            raise forms.ValidationError('le champ "arrival_min" doit être un nombre entre 0 et 60 !')
        return arrival_min

    def clean_duration_hours(self):
        duration_hours = self.cleaned_data['duration_hours']
        if not isinstance(duration_hours, int):
            raise forms.ValidationError('le champ "duration_hours" ne doit contenir qu\'un nombre !')
        return duration_hours

    def clean_duration_min(self):
        duration_min = self.cleaned_data['duration_min']
        if not (0 <= duration_min < 60):
            raise forms.ValidationError('le champ "duration_min" doit être un nombre entre 0 et 60 !')
        return duration_min

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get('departure')
        destination = cleaned_data.get('destination')
        if source and destination and not validate_source_destination(source, destination):
            raise forms.ValidationError('La source et la destination doivent être différentes et non vides.')
        dep_hours = cleaned_data.get('dep_hours')
        dep_min = cleaned_data.get('dep_min')
        arrival_hours = cleaned_data.get('arrival_hours')
        arrival_min = cleaned_data.get('arrival_min')
        if (dep_hours is not None and dep_min is not None and not validate_time(dep_hours, dep_min)) or \
           (arrival_hours is not None and arrival_min is not None and not validate_time(arrival_hours, arrival_min)):
            raise forms.ValidationError('Les heures et minutes de départ et d\'arrivée doivent être valides.')
        duration_hours = cleaned_data.get('duration_hours')
        duration_min = cleaned_data.get('duration_min')
        if not validate_duration(duration_hours, duration_min):
            raise forms.ValidationError('La durée doit être valide.')

        return cleaned_data
