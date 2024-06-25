from EDA import load_data, show_basic_info, plot_histogram, plot_boxplot

def main():
    # Chemin vers votre fichier CSV
    csv_path = r'C:\Users\gchupe\flightPredict\dataset\rawData\flight_dataset.csv'
    
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

if __name__ == "__main__":
    main()
