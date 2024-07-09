import pytest
import pandas as pd
from validation_data.validate_data_types import valider_types_donnees, valider_qualite_donnees, pipeline_validation_donnees

@pytest.fixture
def df_valid():
    return pd.DataFrame({
        'Airline': ['IndiGo', 'Air India', 'Jet Airways'],
        'Source': ['Banglore', 'Kolkata', 'Delhi'],
        'Destination': ['New Delhi', 'Banglore', 'Cochin'],
        'Total_Stops': [0, 2, 2],
        'Price': [3897, 7662, 13882],
        'Date': [24, 1, 9],
        'Month': [3, 5, 6],
        'Year': [2019, 2019, 2019],
        'Dep_hours': [22, 5, None],
        'Dep_min': [20, 50, 25],
        'Arrival_hours': [1, 13, 4],
        'Arrival_min': [10, 15, 25],
        'Duration_hours': [2, 7, 19],
        'Duration_min': [50, 25, 0]
    })

@pytest.fixture
def types_attendus():
    return {
        'Airline': 'object',
        'Source': 'object',
        'Destination': 'object',
        'Total_Stops': 'int64',
        'Price': 'int64',
        'Date': 'int64',
        'Month': 'int64',
        'Year': 'int64',
        'Dep_hours': 'int64',
        'Dep_min': 'int64',
        'Arrival_hours': 'int64',
        'Arrival_min': 'int64',
        'Duration_hours': 'int64',
        'Duration_min': 'int64',
    }

def test_valider_types_donnees(df_valid, types_attendus):
    resultats = valider_types_donnees(df_valid, types_attendus)
    for colonne, resultat in resultats.items():
        assert resultat['valid'], f"Type mismatch in column {colonne}: expected {resultat['expected']}, got {resultat['actual']}"

def test_valider_qualite_donnees(df_valid):
    resultats = valider_qualite_donnees(df_valid)
    for colonne, valeur in resultats['valeurs_manquantes'].items():
        assert valeur == 0, f"Missing values found in column {colonne}"

    for colonne, valeur in resultats['valeurs_negatives'].items():
        assert valeur == 0, f"Negative values found in column {colonne}"

    for colonne, valeur in resultats['valeurs_hors_plage'].items():
        assert valeur == 0, f"Out of range values found in column {colonne}"

def test_pipeline_validation_donnees(df_valid, types_attendus):
    resultats = pipeline_validation_donnees(df_valid, types_attendus)
    for colonne, resultat in resultats['validation_types'].items():
        assert resultat['valid'], f"Type mismatch in column {colonne}: expected {resultat['expected']}, got {resultat['actual']}"

    for colonne, valeur in resultats['qualite_donnees']['valeurs_manquantes'].items():
        assert valeur == 0, f"Missing values found in column {colonne}"

    for colonne, valeur in resultats['qualite_donnees']['valeurs_negatives'].items():
        assert valeur == 0, f"Negative values found in column {colonne}"

    for colonne, valeur in resultats['qualite_donnees']['valeurs_hors_plage'].items():
        assert valeur == 0, f"Out of range values found in column {colonne}"
