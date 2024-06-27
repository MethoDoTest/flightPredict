# test_validation.py
import pandas as pd

from data_quality import validation


def test_validate_airline():
    assert validation.validate_airline("Airline") is True
    assert validation.validate_airline("") is False
    assert validation.validate_airline(None) is False


def test_validate_source_destination():
    assert validation.validate_source_destination("Source", "Destination") is True
    assert validation.validate_source_destination("Source", "Source") is False
    assert validation.validate_source_destination("", "Destination") is False


def test_validate_total_stops():
    assert validation.validate_total_stops(0) is True
    assert validation.validate_total_stops(1) is True
    assert validation.validate_total_stops(-1) is False


def test_validate_price():
    assert validation.validate_price(100) is True
    assert validation.validate_price(0) is False
    assert validation.validate_price(-100) is False


def test_validate_date():
    assert validation.validate_date(1, 1, 2020) is True
    assert validation.validate_date(31, 12, 2020) is True
    assert validation.validate_date(32, 1, 2020) is False


def test_validate_time():
    assert validation.validate_time(0, 0) is True
    assert validation.validate_time(23, 59) is True
    assert validation.validate_time(24, 0) is False


def test_validate_duration():
    assert validation.validate_duration(1, 0) is True
    assert validation.validate_duration(0, 59) is True
    assert validation.validate_duration(-1, 0) is False


def test_validate_row():
    row = {
        'Airline': 'Airline',
        'Source': 'Source',
        'Destination': 'Destination',
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
    }
    assert validation.validate_row(row) is True


def test_validate_table():
    data = {
        'Airline': ['Airline'],
        'Source': ['Source'],
        'Destination': ['Destination'],
        'Total_Stops': [1],
        'Price': [100],
        'Date': [1],
        'Month': [1],
        'Year': [2020],
        'Dep_hours': [10],
        'Dep_min': [30],
        'Arrival_hours': [12],
        'Arrival_min': [45],
        'Duration_hours': [2],
        'Duration_min': [15]
    }
    df = pd.DataFrame(data)
    assert validation.validate_table(df) is True


def test_validate_table_wrong_columns():
    data = {
        'Airline': ['Airline'],
        'Source': ['Source'],
        'Destination': ['Destination'],
        'Total_Stops': [1],
        'Price': [100],
        'Date': [1],
        'Month': [1],
        'Year': [2020],
        'Dep_hours': [10],
        'Dep_min': [30],
        'Arrival_hours': [12],
        'Arrival_min': [45],
        'Duration_hours': [2],
        'Duration_min': [15],
        'Extra_column': [0]  # This makes the column count 15
    }

    df = pd.DataFrame(data)
    assert validation.validate_table(df) is False
