# mon_application/forms.py
from django import forms


class PredictionForm(forms.Form):
    input_data = forms.CharField(label="Données", max_length=100)
