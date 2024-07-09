# test_validation.py
import pytest
import pandas as pd
from travel.validation import *


def test_validate_airline():
    assert validate_airline("Airline") is True
    assert validate_airline("") is False
    assert validate_airline(None) is False


def test_validate_source_destination():
    assert validate_source_destination("Source", "Destination") is True
    assert validate_source_destination("Source", "Source") is False
    assert validate_source_destination("", "Destination") is False


def test_validate_total_stops():
    assert validate_total_stops(0) is True
    assert validate_total_stops(1) is True
    assert validate_total_stops(-1) is False


def test_validate_price():
    assert validate_price(100) is True
    assert validate_price(0) is False
    assert validate_price(-100) is False


def test_validate_date():
    assert validate_date(1, 1, 2020) is True
    assert validate_date(31, 12, 2020) is True
    assert validate_date(32, 1, 2020) is False


def test_validate_time():
    assert validate_time(0, 0) is True
    assert validate_time(23, 59) is True
    assert validate_time(24, 0) is False


def test_validate_duration():
    assert validate_duration(1, 0) is True
    assert validate_duration(0, 59) is True
    assert validate_duration(-1, 0) is False


def test_validate_row():
    row = {
        "Airline": "Airline",
        "Source": "Source",
        "Destination": "Destination",
        "Total_Stops": 1,
        "Price": 100,
        "Date": 1,
        "Month": 1,
        "Year": 2020,
        "Dep_hours": 10,
        "Dep_min": 30,
        "Arrival_hours": 12,
        "Arrival_min": 45,
        "Duration_hours": 2,
        "Duration_min": 15,
    }
    assert validate_row(row) is True


def test_validate_table():
    data = {
        "Airline": ["Airline"],
        "Source": ["Source"],
        "Destination": ["Destination"],
        "Total_Stops": [1],
        "Price": [100],
        "Date": [1],
        "Month": [1],
        "Year": [2020],
        "Dep_hours": [10],
        "Dep_min": [30],
        "Arrival_hours": [12],
        "Arrival_min": [45],
        "Duration_hours": [2],
        "Duration_min": [15],
    }
    df = pd.DataFrame(data)
    assert validate_table(df) is True


def test_validate_table_wrong_columns():
    data = {
        "Airline": ["Airline"],
        "Source": ["Source"],
        "Destination": ["Destination"],
        "Total_Stops": [1],
        "Price": [100],
        "Date": [1],
        "Month": [1],
        "Year": [2020],
        "Dep_hours": [10],
        "Dep_min": [30],
        "Arrival_hours": [12],
        "Arrival_min": [45],
        "Duration_hours": [2],
        "Duration_min": [15],
        "Extra_column": [0],
    }

    df = pd.DataFrame(data)
    assert validate_table(df) is False
