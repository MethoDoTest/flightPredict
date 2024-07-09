from EDA import (load_data, show_basic_info, plot_histogram, plot_boxplot,
                 analyze_missing_values, generate_feature_report,
                 plot_correlation_matrix, create_new_features)

def main():
    csv_path = 'dataset/rawData/flight_dataset.csv'
    output_path = 'dataset/rawData/flight_dataset_features.csv'
    
    # Charger les données
    df = load_data(csv_path)
    
    # Créer de nouvelles caractéristiques
    print("\nCréation de nouvelles caractéristiques :")
    df_with_new_features = create_new_features(df)
    
    # Sauvegarder le nouveau DataFrame avec les nouvelles caractéristiques
    df_with_new_features.to_csv(output_path, index=False)
    print(f"Le nouveau dataset avec les nouvelles caractéristiques a été sauvegardé sous {output_path}")

if __name__ == "__main__":
    main()
