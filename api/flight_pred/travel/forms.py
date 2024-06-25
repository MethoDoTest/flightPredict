from django import forms
import re

class TravelForm(forms.Form):
    departure = forms.CharField(label='depart', max_length=100, required=True)
    destination = forms.CharField(label='destination', max_length=100, required=True)

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
    