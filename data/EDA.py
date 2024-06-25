import pandas as pd
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
