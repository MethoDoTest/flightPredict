import pytest
import pandas as pd
from processing_fonction import (load_data)

@pytest.fixture
def sample_data():
    data = {
        "Airline": ["IndiGo", "Air India"],
        "Source": ["Delhi", "Kolkata"],
        "Destination": ["Cochin", "Delhi"],
        "Total_Stops": [1, 0],
        "Price": [3000, 5000],
        "Date": [1, 2],
        "Month": [1, 1],
        "Year": [2020, 2020],
        "Dep_hours": [5, 6],
        "Dep_min": [30, 45],
        "Arrival_hours": [7, 8],
        "Arrival_min": [0, 15],
        "Duration_hours": [2, 2],
        "Duration_min": [30, 45]
    }
    return pd.DataFrame(data)

# Fixture pour le chemin du fichier CSV de données d'entrée
@pytest.fixture
def inputData(tmp_path, sample_data):
    file_path = tmp_path / "./dataset/rawData/flight_dataset.csv"  
    sample_data.to_csv(file_path, index=False)  
    return file_path 

# Tests

def testLoadDataFromDataframe(sample_data):
    df = load_data(sample_data, dataFrame=True)
    assert not df.empty, "Le DataFrame est vide"

def testDataframeEmpty(input_data):
    df = load_data(input_data)
    assert isinstance(df, pd.DataFrame), "Les données chargées ne sont pas un DataFrame"

def testColumnNames(input_data):
    df = load_data(input_data)
    expected_columns = [
        "Airline", "Source", "Destination", "Total_Stops", "Price", 
        "Date", "Month", "Year", "Dep_hours", "Dep_min", 
        "Arrival_hours", "Arrival_min", "Duration_hours", "Duration_min"
    ]
    assert list(df.columns) == expected_columns, "Les colonnes du DataFrame ne correspondent pas aux colonnes attendues"

def test_empty_dataframe(input_data):
    df = load_data(input_data)
    assert not df.empty, "Le DataFrame est vide"
    assert len(df.columns) != 0, "Le DataFrame n'a pas de colonnes"