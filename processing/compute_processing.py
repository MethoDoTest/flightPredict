import pandas as pd
from processing_fonction import load_data, analyze_missing_values, impute_missing_values, generate_feature_report, create_new_features, preprocess_data

def main():
    # Chemin du fichier (utilisez un chemin absolu)
    file_path = '..\\dataset\\rawData\\flight_dataset.csv'

    # Chargement des données
    df = load_data(file_path)

    # Analyse des valeurs manquantes
    analyze_missing_values(df)

    # Génération du rapport de caractéristiques
    generate_feature_report(df)

    # Prétraitement des données
    preprocess_data(df)

    # Affichage des premières lignes pour vérifier
    print("Training Features DataFrame:")
    #print(X.head())
    print("\nTarget Series:")
    #print(y.head())

if __name__ == "__main__":
    main()
