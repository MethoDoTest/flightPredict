import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from EDA import (load_data, show_basic_info, plot_histogram, plot_boxplot,
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
    df = load_data('dataset/rawData/flight_dataset.csv')
    assert isinstance(df, pd.DataFrame)

def test_show_basic_info(sample_data, capsys):
    show_basic_info(sample_data)
    captured = capsys.readouterr()
    assert "RangeIndex" in captured.out
    assert "Data columns" in captured.out

def test_plot_histogram(sample_data):
    plot_histogram(sample_data, 'Arrival_hours')
    # Visuellement vérifier l'histogramme
    plt.close()

def test_plot_boxplot(sample_data):
    plot_boxplot(sample_data, 'Total_Stops')
    # Visuellement vérifier le boxplot
    plt.close()

def test_analyze_missing_values(sample_data):
    analyze_missing_values(sample_data)
    # Visuellement vérifier la heatmap
    plt.close()

def test_generate_feature_report(sample_data):
    generate_feature_report(sample_data)
    # Visuellement vérifier l'histogramme
    plt.close()

def test_create_new_features(sample_data):
    df_with_new_features = create_new_features(sample_data)
    assert 'Flight_Date' in df_with_new_features.columns
    assert 'Day_of_Week' in df_with_new_features.columns
    assert 'Season' in df_with_new_features.columns
    assert 'Is_Holiday' in df_with_new_features.columns

def test_plot_correlation_matrix(sample_data):
    plot_correlation_matrix(sample_data)
    # Visuellement vérifier la matrice de corrélation
    plt.close()

def test_plot_price_vs_date_features(sample_data):
    df_with_new_features = create_new_features(sample_data)
    plot_price_vs_date_features(df_with_new_features)
    # Visuellement vérifier les boxplots
    plt.close()
