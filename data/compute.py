from EDA import load_data, show_basic_info, plot_histogram, plot_boxplot, analyze_missing_values, generate_feature_report, plot_correlation_matrix, plot_pairplot, plot_scatter, create_new_features, plot_price_vs_date_features

def main():

    csv_path = r'dataset\rawData\flight_dataset.csv'
    
    # Charger les données
    df = load_data(csv_path)
    
    # Afficher les informations de base
    print("Informations de base sur le DataFrame :")
    show_basic_info(df)
    
    # Afficher un histogramme de la colonne 'Arrival_hours'
    print("\nAffichage de l'histogramme pour 'Arrival_hours' :")
    plot_histogram(df, 'Arrival_hours')
    
    # Afficher un boxplot de la colonne 'Total_Stops'
    print("\nAffichage du boxplot pour 'Total_Stops' :")
    plot_boxplot(df, 'Total_Stops')

    # Analyser les valeurs manquantes
    print("\nAnalyse des valeurs manquantes :")
    analyze_missing_values(df)
    
    # Générer un rapport sur les nouvelles caractéristiques potentielles
    print("\nGénération du rapport de feature engineering :")
    generate_feature_report(df)

    # Afficher la matrice de corrélation
    print("\nAffichage de la matrice de corrélation :")
    plot_correlation_matrix(df)

    # Créer de nouvelles caractéristiques
    print("\nCréation de nouvelles caractéristiques :")
    df = create_new_features(df)

    # Analyser les prix par rapport aux nouvelles caractéristiques de date
    print("\nAnalyse des prix par rapport aux nouvelles caractéristiques de date :")
    plot_price_vs_date_features(df)

if __name__ == "__main__":
    main()
