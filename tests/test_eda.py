import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from processing.EDA import (load_data, show_basic_info, plot_histogram, plot_boxplot,
                            analyze_missing_values, generate_feature_report,
                            plot_correlation_matrix, create_new_features, plot_price_vs_date_features)


@pytest.fixture
def sample_data():
    data = {
        "Airline": ["IndiGo", "Air India", "Jet Airways", "IndiGo", "IndiGo"],
        "Source": ["Banglore", "Kolkata", "Delhi", "Kolkata", "Banglore"],
        "Destination": ["New Delhi", "Banglore", "Cochin", "Banglore", "New Delhi"],
        "Total_Stops": [0, 2, 2, 1, 1],
        "Price": [3897, 7662, 13882, 6218, 13302],
        "Date": [24, 1, 9, 12, 1],
        "Month": [3, 5, 6, 5, 3],
        "Year": [2019, 2019, 2019, 2019, 2019],
        "Dep_hours": [22, 5, 9, 18, 16],
        "Dep_min": [20, 50, 25, 5, 50],
        "Arrival_hours": [1, 13, 4, 23, 21],
        "Arrival_min": [10, 15, 25, 30, 35],
        "Duration_hours": [2, 7, 19, 5, 4],
        "Duration_min": [50, 25, 0, 25, 45]
    }
    return pd.DataFrame(data)


def test_load_data():
    print("Test: Load Data")
    df = load_data('dataset/flight_dataset.csv')
    assert isinstance(df, pd.DataFrame)
    print("Test Load Data: Validated")


def test_show_basic_info(sample_data, capsys):
    print("Test: Show Basic Info")
    show_basic_info(sample_data)
    captured = capsys.readouterr()
    assert "RangeIndex" in captured.out
    assert "Data columns" in captured.out
    print("Test Show Basic Info: Validated")


def test_create_new_features(sample_data):
    print("Test: Create New Features")
    df_with_new_features = create_new_features(sample_data)
    assert 'Flight_Date' in df_with_new_features.columns
    assert 'Day_of_Week' in df_with_new_features.columns
    assert 'Season' in df_with_new_features.columns
    assert 'Is_Holiday' in df_with_new_features.columns
    print("Test Create New Features: Validated")
