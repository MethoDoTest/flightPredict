import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Charge le fichier CSV dans un DataFrame Pandas."""
    return pd.read_csv(file_path)

def analyze_missing_values(df):
    """Analyse et affiche les valeurs manquantes dans le DataFrame."""
    missing_values = df.isnull().sum()
    print("Valeurs manquantes par colonne :")
    print(missing_values)

    if missing_values.any():
        plt.figure(figsize=(12, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Heatmap des valeurs manquantes')
        plt.show()
    else:
        print("Aucune valeur manquante détectée.")

def impute_missing_values(df):
    """Impute les valeurs manquantes avec la moyenne des colonnes."""
    missing_values = df.isnull().sum()
    if missing_values.any():
        for col in df.columns:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mean(), inplace=True)
        print("Imputation des valeurs manquantes effectuée.")
    else:
        print("Aucune valeur manquante à imputer.")
    return df

def generate_feature_report(df):
    """Génère un rapport sur les nouvelles caractéristiques potentielles."""
    print("Analyse des caractéristiques existantes pour le feature engineering :")
    df['Total_Duration_Minutes'] = df['Duration_hours'] * 60 + df['Duration_min']
    print("Nouvelle caractéristique 'Total_Duration_Minutes' créée.")

def create_new_features(df):
    """Crée de nouvelles caractéristiques basées sur les données existantes."""
    df = df.rename(columns={'Date': 'Day'})
    df['Flight_Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df['Day_of_Week'] = df['Flight_Date'].dt.day_name()
    df['Season'] = df['Flight_Date'].apply(lambda x: (x.month % 12 + 3) // 3)
    df['Season'] = df['Season'].replace({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
    df['Is_Holiday'] = df['Flight_Date'].apply(is_holiday)
    print("Nouvelles caractéristiques créées : 'Flight_Date', 'Day_of_Week', 'Season' et 'Is_Holiday'")
    return df

def is_holiday(date):
    """Détermine si une date donnée est une période de vacances."""
    holidays = [
        (pd.Timestamp(date.year, 12, 20), pd.Timestamp(date.year, 12, 31)),
        (pd.Timestamp(date.year, 7, 1), pd.Timestamp(date.year, 8, 31)),
        (pd.Timestamp(date.year, 4, 1), pd.Timestamp(date.year, 4, 15))
    ]
    return any(start <= date <= end for start, end in holidays)

def preprocess_data(df):
    """Prépare les données pour l'entraînement."""
    categorical_cols = ['Airline', 'Source', 'Destination', 'Day_of_Week', 'Season']
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    X = df_encoded.drop(columns=['Price', 'Flight_Date', 'Is_Holiday'])
    y = df_encoded['Price']
    return X, y
