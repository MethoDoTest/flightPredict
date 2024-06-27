# test_validation.py
# import pytest
# import pandas as pd
# from validation import *
#
#
# def test_validate_airline():
#    assert validate_airline("Airline") == True
#    assert validate_airline("") == False
#    assert validate_airline(None) == False
#
#
# def test_validate_source_destination():
#    assert validate_source_destination("Source", "Destination") == True
#    assert validate_source_destination("Source", "Source") == False
#    assert validate_source_destination("", "Destination") == False
#
#
# def test_validate_total_stops():
#    assert validate_total_stops(0) == True
#    assert validate_total_stops(1) == True
#    assert validate_total_stops(-1) == False


# def test_validate_price():
#    assert validate_price(100) == True
#    assert validate_price(0) == False
#    assert validate_price(-100) == False
#
#
# def test_validate_date():
#    assert validate_date(1, 1, 2020) == True
#    assert validate_date(31, 12, 2020) == True
#    assert validate_date(32, 1, 2020) == False
#
#
# def test_validate_time():
#    assert validate_time(0, 0) == True
#    assert validate_time(23, 59) == True
#    assert validate_time(24, 0) == False
#
#
# def test_validate_duration():
#    assert validate_duration(1, 0) == True
#    assert validate_duration(0, 59) == True
#    assert validate_duration(-1, 0) == False


# def test_validate_row():
#    row = {
#        "Airline": "Airline",
#        "Source": "Source",
#        "Destination": "Destination",
#        "Total_Stops": 1,
#        "Price": 100,
#        "Date": 1,
#        "Month": 1,
#        "Year": 2020,
#        "Dep_hours": 10,
#        "Dep_min": 30,
#        "Arrival_hours": 12,
#        "Arrival_min": 45,
#        "Duration_hours": 2,
#        "Duration_min": 15,
#    }
#    assert validate_row(row) == True
#
#
# def test_validate_table():
#    data = {
#        "Airline": ["Airline"],
#        "Source": ["Source"],
#        "Destination": ["Destination"],
#        "Total_Stops": [1],
#        "Price": [100],
#        "Date": [1],
#        "Month": [1],
#        "Year": [2020],
#        "Dep_hours": [10],
#        "Dep_min": [30],
#        "Arrival_hours": [12],
#        "Arrival_min": [45],
#        "Duration_hours": [2],
#        "Duration_min": [15],
#    }
#    df = pd.DataFrame(data)
#    assert validate_table(df) == True
#
#
# def test_validate_table_wrong_columns():
#    data = {
#        "Airline": ["Airline"],
#        "Source": ["Source"],
#        "Destination": ["Destination"],
#        "Total_Stops": [1],
#        "Price": [100],
#        "Date": [1],
#        "Month": [1],
#        "Year": [2020],
#        "Dep_hours": [10],
#        "Dep_min": [30],
#        "Arrival_hours": [12],
#        "Arrival_min": [45],
#        "Duration_hours": [2],
#        "Duration_min": [15],
#        "Extra_column": [0],  # This makes the column count 15
#    }
#
#    df = pd.DataFrame(data)
#    assert validate_table(df) == False
#
