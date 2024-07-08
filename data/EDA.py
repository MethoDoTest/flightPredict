import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Charge le fichier CSV dans un DataFrame Pandas."""
    return pd.read_csv(file_path)

def show_basic_info(df):
    """Affiche les informations de base du DataFrame."""
    print(df.info())
    print(df.describe())

def plot_histogram(df, column):
    """Affiche un histogramme pour une colonne donnée du DataFrame."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogramme de {column}')
    plt.show()

def plot_boxplot(df, column):
    """Affiche un boxplot pour une colonne donnée du DataFrame."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot de {column}')
    plt.show()

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

def generate_feature_report(df):
    """Génère un rapport sur les nouvelles caractéristiques potentielles."""
    print("Analyse des caractéristiques existantes pour le feature engineering :")
    
    # Création de nouvelles caractéristiques à partir de 'Duration_hours' et 'Duration_min'
    df['Total_Duration_Minutes'] = df['Duration_hours'] * 60 + df['Duration_min']
    print("Nouvelle caractéristique 'Total_Duration_Minutes' créée.")

    plt.figure(figsize=(10, 6))
    sns.histplot(df['Total_Duration_Minutes'], kde=True)
    plt.title('Histogramme de Total_Duration_Minutes')
    plt.show()

def plot_correlation_matrix(df):
    """Affiche la matrice de corrélation du DataFrame."""
    correlation_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Matrice de corrélation')
    plt.show()

def plot_pairplot(df):
    """Affiche une paire de graphiques pour visualiser les relations entre plusieurs variables."""
    plt.figure(figsize=(10, 6))
    sns.pairplot(df)
    plt.show()

def plot_scatter(df, x_column, y_column):
    """Affiche un graphique de dispersion pour visualiser la relation entre deux colonnes du DataFrame."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_column], y=df[y_column])
    plt.title(f'Scatter plot de {x_column} vs {y_column}')
    plt.show()

def create_new_features(df):
    """Crée de nouvelles caractéristiques basées sur les données existantes."""
    # Renommer la colonne 'Date' en 'Day'
    df = df.rename(columns={'Date': 'Day'})
    
    # Combiner 'Day', 'Month' et 'Year' en une seule colonne 'Flight_Date'
    df['Flight_Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    
    # Extraire le jour de la semaine de 'Flight_Date'
    df['Day_of_Week'] = df['Flight_Date'].dt.day_name()
    
    # Extraire la saison du 'Flight_Date'
    df['Season'] = df['Flight_Date'].apply(lambda x: (x.month%12 + 3)//3)
    df['Season'] = df['Season'].replace({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})

    # Identifier les périodes de vacances
    df['Is_Holiday'] = df['Flight_Date'].apply(is_holiday)

    print("Nouvelles caractéristiques créées : 'Flight_Date', 'Day_of_Week', 'Season' et 'Is_Holiday'")
    return df

def is_holiday(date):
    """Détermine si une date donnée est une période de vacances."""
    # Exemple de périodes de vacances
    holidays = [
        (pd.Timestamp(date.year, 12, 20), pd.Timestamp(date.year, 12, 31)), # Vacances de Noël
        (pd.Timestamp(date.year, 7, 1), pd.Timestamp(date.year, 8, 31)),    # Vacances d'été
        (pd.Timestamp(date.year, 4, 1), pd.Timestamp(date.year, 4, 15))     # Vacances de printemps
    ]
    return any(start <= date <= end for start, end in holidays)

def plot_price_vs_date_features(df):
    """Affiche les relations entre les prix et les nouvelles caractéristiques de date."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Season', y='Price', data=df)
    plt.title('Prix des vols par saison')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Day_of_Week', y='Price', data=df)
    plt.title('Prix des vols par jour de la semaine')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Is_Holiday', y='Price', data=df)
    plt.title('Prix des vols pendant les périodes de vacances')
    plt.show()
