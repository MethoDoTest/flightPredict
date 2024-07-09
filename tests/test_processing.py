import pytest
import pandas as pd
from processing.processing_fonction import (load_data)

@pytest.fixture

def sampleData():
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

@pytest.fixture
def inputDataCsv():
    filePathCsv = '..\\dataset\\rawData\\flight_dataset.csv'
    return filePathCsv

@pytest.fixture
def inputDataDf(sampleData):
    filePathDf = pd.DataFrame(sampleData)
    return filePathDf

# Tests

def testLoadDataFromDataframe(inputDataDf):
    df = load_data(inputDataDf, dataFrame=True)
    assert not df.empty, "Le DataFrame est vide"

def testDataframeEmpty(inputDataCsv):
    df = load_data(inputDataCsv)
    assert isinstance(df, pd.DataFrame), "Les données chargées ne sont pas un DataFrame"

def testColumnNames(inputDataCsv):
    df = load_data(inputDataCsv)
    expectedColumns = [
        "Airline", "Source", "Destination", "Total_Stops", "Price",
        "Date", "Month", "Year", "Dep_hours", "Dep_min",
        "Arrival_hours", "Arrival_min", "Duration_hours", "Duration_min"
    ]
    assert list(df.columns) == expectedColumns, "Les colonnes du DataFrame ne correspondent pas aux colonnes attendues"

def testEmptyDataframe(inputDataCsv):
    df = load_data(inputDataCsv)
    assert not df.empty, "Le DataFrame est vide"
    assert len(df.columns) != 0, "Le DataFrame n'a pas de colonnes"
