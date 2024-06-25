from django import forms

class TravelForm(forms.Form):
    departure = forms.CharField(label='départ', max_length=100)
    destination = forms.CharField(label='destination', max_length=100)
