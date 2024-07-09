# validation.py

import pandas as pd


def validate_airline(airline):
    """Valide que la compagnie aérienne est une chaîne non vide."""
    return isinstance(airline, str) and airline.strip() != ""


def validate_source_destination(source, destination):
    """Valide que la source et la destination sont des chaînes non vides et différentes."""
    return (
        isinstance(source, str)
        and source.strip() != ""
        and isinstance(destination, str)
        and destination.strip() != ""
        and source != destination
    )


def validate_total_stops(total_stops):
    """Valide que le nombre total d'arrêts est un entier non négatif."""
    return isinstance(total_stops, int) and total_stops >= 0


def validate_price(price):
    """Valide que le prix est un entier positif."""
    return isinstance(price, int) and price > 0


def validate_date(date, month, year):
    """Valide que la date, le mois et l'année forment une date valide."""
    try:
        pd.Timestamp(year, month, date)
        return True
    except ValueError:
        return False


def validate_time(hour, minute):
    """Valide que l'heure et les minutes forment un temps valide."""
    return (
        isinstance(hour, int)
        and 0 <= hour < 24
        and isinstance(minute, int)
        and 0 <= minute < 60
    )


def validate_duration(hours, minutes):
    """Valide que la durée en heures et minutes est valide."""
    return (
        isinstance(hours, int)
        and hours >= 0
        and isinstance(minutes, int)
        and 0 <= minutes < 60
    )


def validate_row(row):
    """Valide une ligne du tableau."""
    return (
        validate_airline(row["Airline"])
        and validate_source_destination(row["Source"], row["Destination"])
        and validate_total_stops(row["Total_Stops"])
        and validate_price(row["Price"])
        and validate_date(row["Date"], row["Month"], row["Year"])
        and validate_time(row["Dep_hours"], row["Dep_min"])
        and validate_time(row["Arrival_hours"], row["Arrival_min"])
        and validate_duration(row["Duration_hours"], row["Duration_min"])
    )


def validate_table(df):
    """Valide tout le tableau et s'assure qu'il y a bien 14 colonnes."""
    return True if (df.shape[1] == 14 and df.apply(validate_row, axis=1).all()) else False
