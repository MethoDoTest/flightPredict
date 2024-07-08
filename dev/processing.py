import pandas as pd

def encoder_categorielles(df, colonnes_categorielles):
    """
    Encoder les variables catégorielles en utilisant l'encodage one-hot.

    Paramètres :
    df (DataFrame) : Le dataframe d'entrée.
    colonnes_categorielles (liste) : Liste des colonnes à encoder.

    Retourne :
    DataFrame : Le dataframe avec les variables catégorielles encodées.
    """
    return pd.get_dummies(df, columns=colonnes_categorielles, drop_first=True)

def separer_features_target(df, colonne_target):
    """
    Séparer le dataframe en features et target.

    Paramètres :
    df (DataFrame) : Le dataframe d'entrée.
    colonne_target (str) : Le nom de la colonne target.

    Retourne :
    DataFrame, Series : Le dataframe des features et la series target.
    """
    X = df.drop(columns=[colonne_target])
    y = df[colonne_target]
    return X, y

def pretraiter_donnees(df, colonnes_categorielles, colonne_target):
    """
    Prétraiter le dataframe d'entrée en encodant les variables catégorielles,
    en enrichissant les données et en séparant les features et target.

    Paramètres :
    df (DataFrame) : Le dataframe d'entrée.
    colonnes_categorielles (liste) : Liste des colonnes catégorielles à encoder.
    colonne_target (str) : Le nom de la colonne target.

    Retourne :
    DataFrame, Series : Les features et target prétraités.
    """
    df_encode = encoder_categorielles(df, colonnes_categorielles)

    X, y = separer_features_target(df_encode, colonne_target)
    return X, y

# Exemple d'utilisation :
# Charger le dataset
df = pd.read_csv('..\\dataset\\rawData\\flight_dataset.csv')
print('summary of data', df.head())

# Définir les colonnes catégorielles et la colonne cible
colonnes_categorielles = ['Airline', 'Source', 'Destination']
colonne_target = 'Price'

# Prétraiter les données
X, y = pretraiter_donnees(df, colonnes_categorielles, colonne_target)

# Afficher les résultats
print("Features DataFrame:")
print(X.head())

print("\nTarget Series:")
print(y.head())

