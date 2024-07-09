#test_validation.py

import pytest
import pandas as pd

# Importer les fonctions de validation depuis validation.py
from validation import (
    validate_airline,
    validate_source_destination,
    validate_total_stops,
    validate_price,
    validate_date,
    validate_time,
    validate_duration,
    validate_row,
    validate_table
)

# Fixture pour créer un DataFrame de test
@pytest.fixture
def sample_dataframe():
    data = {
        'Airline': ['Airline A', 'Airline B', 'Airline C'],
        'Source': ['City A', 'City B', 'City C'],
        'Destination': ['City X', 'City Y', 'City Z'],
        'Total_Stops': [1, 2, 1],
        'Price': [100, 150, 200],
        'Date': [1, 1, 1],
        'Month': [1, 1, 1],
        'Year': [2020, 2020, 2020],
        'Dep_hours': [10, 12, 10],
        'Dep_min': [30, 0, 30],
        'Arrival_hours': [12, 14, 12],
        'Arrival_min': [45, 30, 45],
        'Duration_hours': [2, 2, 2],
        'Duration_min': [15, 30, 15]
    }
    return pd.DataFrame(data)

def test_validate_airline():
    assert validate_airline("Airline A") == True
    assert validate_airline("") == False
    assert validate_airline(123) == False

def test_validate_source_destination():
    assert validate_source_destination("City A", "City B") == True
    assert validate_source_destination("", "City B") == False
    assert validate_source_destination("City A", "City A") == False
    assert validate_source_destination(123, "City B") == False

def test_validate_total_stops():
    assert validate_total_stops(1) == True
    assert validate_total_stops(0) == True
    assert validate_total_stops(-1) == False
    assert validate_total_stops("1") == False

def test_validate_price():
    assert validate_price(100) == True
    assert validate_price(0) == False
    assert validate_price(-100) == False
    assert validate_price("100") == False

def test_validate_date():
    assert validate_date(1, 1, 2020) == True
    assert validate_date(32, 1, 2020) == False  # Jour invalide
    assert validate_date(1, 13, 2020) == False  # Mois invalide
    assert validate_date("1", "1", "2020") == False

def test_validate_time():
    assert validate_time(10, 30) == True
    assert validate_time(24, 0) == False  # Heure invalide
    assert validate_time(12, -1) == False  # Minute invalide
    assert validate_time("10", "30") == False

def test_validate_duration():
    assert validate_duration(2, 30) == True
    assert validate_duration(0, 60) == False  # Heure invalide
    assert validate_duration(-1, 30) == False  # Heure invalide
    assert validate_duration("2", "30") == False

def test_validate_row(sample_dataframe):
    valid_row = pd.Series({
        'Airline': 'airplane',
        'Source': 'Toronto',
        'Destination': 'Los Angeles',
        'Total_Stops': 1,
        'Price': 100,
        'Date': 1,
        'Month': 1,
        'Year': 2020,
        'Dep_hours': 10,
        'Dep_min': 30,
        'Arrival_hours': 12,
        'Arrival_min': 45,
        'Duration_hours': 2,
        'Duration_min': 15
    })

    invalid_row = pd.Series({
        'Airline': '',
        'Source': 'Toronto',
        'Destination': 'Los Angeles',
        'Total_Stops': 1,
        'Price': 100,
        'Date': 1,
        'Month': 1,
        'Year': 2020,
        'Dep_hours': 10,
        'Dep_min': 30,
        'Arrival_hours': 12,
        'Arrival_min': 45,
        'Duration_hours': 2,
        'Duration_min': 15
    })

    assert validate_row(valid_row) == True
    assert validate_row(invalid_row) == False

def test_validate_table(sample_dataframe):
    assert validate_table(sample_dataframe) == True

    # Test avec un DataFrame invalide (ajouter une ligne invalide)
    invalid_df = sample_dataframe.copy()
    invalid_df.at[1, 'Price'] = 0
    assert validate_table(invalid_df) == False