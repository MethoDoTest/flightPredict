import pytest
import pandas as pd
from EDA import load_data, show_basic_info, plot_histogram, plot_boxplot

@pytest.fixture
def sample_data():
    data = {
        "Airline": ["IndiGo", "Air India", "Jet Airways", "IndiGo", "IndiGo"],
        "Source": ["Banglore", "Kolkata", "Delhi", "Kolkata", "Banglore"],
        "Destination": ["New Delhi", "Banglore", "Cochin", "Banglore", "New Delhi"],
        "Total_Stops": [0, 2, 2, 1, 1],
        "Arrival_hours": [1, 13, 4, 23, 21],
        "Arrival_min": [10, 15, 25, 30, 35],
        "Duration_hours": [2, 7, 19, 5, 4],
        "Duration_min": [50, 25, 0, 25, 45]
    }
    return pd.DataFrame(data)

def test_load_data():
    df = load_data('C:\\Users\\gchupe\\flightPredict\\dataset\\rawData\\flight_dataset.csv')
    assert isinstance(df, pd.DataFrame)

def test_show_basic_info(sample_data, capsys):
    show_basic_info(sample_data)
    captured = capsys.readouterr()
    assert "RangeIndex" in captured.out
    assert "Data columns" in captured.out

def test_plot_histogram(sample_data):
    plot_histogram(sample_data, 'Arrival_hours')
    # Visuellement vérifier l'histogramme

def test_plot_boxplot(sample_data):
    plot_boxplot(sample_data, 'Total_Stops')
    # Visuellement vérifier le boxplot
