#validation.py
import pandas as pd

def validate_airline(airline):
    """Valide que la compagnie aérienne est une chaîne non vide."""
    return isinstance(airline, str) and airline.strip() != ""

def validate_source_destination(source, destination):
    """Valide que la source et la destination sont des chaînes non vides et différentes."""
    return isinstance(source, str) and source.strip() != "" and \
           isinstance(destination, str) and destination.strip() != "" and \
           source != destination

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
    return isinstance(hour, int) and 0 <= hour < 24 and \
           isinstance(minute, int) and 0 <= minute < 60

def validate_duration(hours, minutes):
    """Valide que la durée en heures et minutes est valide."""
    return isinstance(hours, int) and hours >= 0 and \
           isinstance(minutes, int) and 0 <= minutes < 60

def validate_row(row):
    results = {
        "Airline": bool(row["Airline"]),
        "SourceDest": row["Source"] != row["Destination"],
        "TotalStops": validate_total_stops(row["Total_Stops"]),
        "Price": validate_price(row["Price"]),
        "Date": validate_date(row["Date"], row["Month"], row["Year"]),
        "DepTime": validate_time(row["Dep_hours"], row["Dep_min"]),
        "ArrivalTime": validate_time(row["Arrival_hours"], row["Arrival_min"]),
        "Duration": validate_duration(row["Duration_hours"], row["Duration_min"]),
        "Consistency": (row["Arrival_hours"] * 60 + row["Arrival_min"] - row["Dep_hours"] * 60 - row["Dep_min"]) ==
                       (row["Duration_hours"] * 60 + row["Duration_min"])
    }
    print(f"Validation results: {results}")
    return all(results.values())


def validate_table(df):
    """Valide tout le tableau."""
    if df.shape[1] != 14:
        return False
    return df.apply(validate_row, axis=1).all()

def detect_outliers(df, column):
    """Détecte les valeurs aberrantes dans une colonne donnée."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def remove_outliers(df, column):
    """Supprime les valeurs aberrantes dans une colonne donnée."""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def check_missing_values(df):
    """Vérifie la présence de valeurs manquantes dans le DataFrame."""
    return df.isnull().sum().sum() == 0

def check_duplicates(df):
    """Vérifie la présence de doublons dans le DataFrame."""
    return df.duplicated().any()

def check_data_consistency(df):
    """Vérifie la cohérence des données entre les colonnes."""
    return (df['Dep_hours'] != df['Arrival_hours']) | (df['Dep_min'] != df['Arrival_min'])

def validate_data_quality(df):
    """Valide la qualité des données en effectuant plusieurs vérifications."""
    return (
        validate_table(df) and
        check_missing_values(df) and
        not check_duplicates(df) and
        check_data_consistency(df)
    )
