import pandas as pd

def valider_types_donnees(df, types_attendus):
    """
    Valide les types de données des colonnes du DataFrame.

    Paramètres:
    df (pd.DataFrame): Le DataFrame à valider.
    types_attendus (dict): Un dictionnaire avec les noms des colonnes comme clés et les types de données attendus comme valeurs.

    Retourne:
    dict: Un dictionnaire avec les résultats de validation pour chaque colonne.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Les données doivent être un DataFrame")

    types_actuels = df.dtypes.to_dict()
    resultats_validation_types = {}

    for colonne, type_attendu in types_attendus.items():
        type_actuel = types_actuels.get(colonne)
        resultats_validation_types[colonne] = {
            "expected": type_attendu,
            "actual": str(type_actuel),
            "valid": str(type_actuel) == type_attendu
        }

    return resultats_validation_types

def valider_qualite_donnees(df):
    """
    Valide la qualité des données du DataFrame.

    Paramètres:
    df (pd.DataFrame): Le DataFrame à valider.

    Retourne:
    dict: Un dictionnaire avec les valeurs manquantes, les valeurs négatives et les valeurs hors plage.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Les données doivent être un DataFrame")

    # Vérifier les valeurs manquantes
    valeurs_manquantes = df.isnull().sum()

    # Vérifier les valeurs négatives dans les colonnes numériques
    valeurs_negatives = df.select_dtypes(include=['int64', 'float64']).lt(0).sum()

    # Vérifier les valeurs hors plage dans les colonnes liées au temps
    colonnes_temps = ['Dep_hours', 'Dep_min', 'Arrival_hours', 'Arrival_min', 'Duration_hours', 'Duration_min']
    valeurs_hors_plage = {}

    for colonne in colonnes_temps:
        if colonne in df.columns:
            nombre_hors_plage = df[(df[colonne] < 0) | (df[colonne] >= 60 if 'min' in colonne else df[colonne] >= 24)][colonne].count()
            valeurs_hors_plage[colonne] = nombre_hors_plage

    return {
        "valeurs_manquantes": valeurs_manquantes,
        "valeurs_negatives": valeurs_negatives,
        "valeurs_hors_plage": valeurs_hors_plage
    }

def pipeline_validation_donnees(df, types_attendus):
    """
    Exécute un pipeline complet de validation des données, incluant la validation des types,
    la validation de la qualité et les tests d'intégration.

    Paramètres:
    df (pd.DataFrame): Le DataFrame à valider.
    types_attendus (dict): Un dictionnaire avec les noms des colonnes comme clés et les types de données attendus comme valeurs.

    Retourne:
    dict: Un dictionnaire avec les résultats de tous les tests de validation.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Les données doivent être un DataFrame")

    # Valider les types de données
    resultats_validation_types = valider_types_donnees(df, types_attendus)

    # Valider la qualité des données
    resultats_qualite_donnees = valider_qualite_donnees(df)

    # Intégrer les résultats
    resultats_validation = {
        "validation_types": resultats_validation_types,
        "qualite_donnees": resultats_qualite_donnees
    }

    return resultats_validation

# Exemple d'utilisation
types_attendus = {
    'Airline': 'object',
    'Source': 'object',
    'Destination': 'object',
    'Total_Stops': 'int64',
    'Price': 'int64',
    'Date': 'int64',
    'Month': 'int64',
    'Year': 'int64',
    'Dep_hours': 'int64',
    'Dep_min': 'int64',
    'Arrival_hours': 'int64',
    'Arrival_min': 'int64',
    'Duration_hours': 'int64',
    'Duration_min': 'int64',
}
# Charger le dataset
chemin_fichier = '../dataset/rawData/flight_dataset.csv'


df = pd.read_csv(chemin_fichier)

# Exécuter le pipeline de validation
resultats_validation = pipeline_validation_donnees(df, types_attendus)

# Afficher les résultats
print("Résultats de la validation des types:")
print(pd.DataFrame(resultats_validation['validation_types']))

print("\nRésultats de la qualité des données - Valeurs manquantes:")
print(resultats_validation['qualite_donnees']['valeurs_manquantes'])

print("\nRésultats de la qualité des données - Valeurs négatives:")
print(resultats_validation['qualite_donnees']['valeurs_negatives'])

print("\nRésultats de la qualité des données - Valeurs hors plage:")
print(pd.DataFrame(resultats_validation['qualite_donnees']['valeurs_hors_plage'], index=[0]).transpose())







