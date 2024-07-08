import pytest
import pandas as pd
from processing_fonction import (load_data)

@pytest.fixture
def sample_data():
    data = {
        'Year': [2020, 1990, 2024],
        'Month': [1, 12, 7],
        'Day': [1, 15, 30],
        'Airline': ['IndiGo', 'Air India', 'Jet Airways'],
        'Source': ['Delhi', 'Kolkata', 'Mumbai'],
        'Destination': ['Cochin', 'Delhi', 'Hyderabad'],
        'Duration_hours': [2, 10, 27],
        'Duration_min': [30, 45, 500],
        'Price': [3000, 5000, 2000]
    }
    df = pd.DataFrame(data)
    return df

def test_dataframe_creation():
    df = load_data('./dataset/rawData/flight_dataset.csv')
    assert isinstance(df, pd.DataFrame), "The object is not a pandas DataFrame"
    assert not df.empty, "The DataFrame is empty"

def test_column_names(sample_data):
    df = load_data('./dataset/rawData/flight_dataset.csv')
    expected_columns = [
    "Airline", "Source", "Destination", "Total_Stops", "Price", 
    "Date", "Month", "Year", "Dep_hours", "Dep_min", 
    "Arrival_hours", "Arrival_min", "Duration_hours", "Duration_min"
]
    assert list(df.columns) == expected_columns, "DataFrame columns do not match the expected columns"

def test_empty_dataframe():
    df = pd.DataFrame()
    assert df.empty, "The DataFrame is not empty"
    assert len(df.columns) == 0, "The DataFrame has columns"



