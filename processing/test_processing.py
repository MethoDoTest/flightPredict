import pytest
import pandas as pd
from processing_fonction import (load_data)

@pytest.fixture

def test_dataframe_creation():
    df = load_data('./dataset/rawData/flight_dataset.csv')
    assert isinstance(df, pd.DataFrame), "The object is not a pandas DataFrame"

def test_column_names():
    df = load_data('./dataset/rawData/flight_dataset.csv')
    expected_columns = [
    "Airline", "Source", "Destination", "Total_Stops", "Price", 
    "Date", "Month", "Year", "Dep_hours", "Dep_min", 
    "Arrival_hours", "Arrival_min", "Duration_hours",  "Duration_min"
    ]
    assert list(df.columns) == expected_columns, "DataFrame columns do not match the expected columns"

def test_empty_dataframe():
    df = load_data('./dataset/rawData/flight_dataset.csv')
    assert not df.empty, "The DataFrame is not empty"
    assert len(df.columns) != 0, "The DataFrame has columns"



