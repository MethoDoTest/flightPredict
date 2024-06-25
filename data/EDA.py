import pandas as pd

# Chemin vers votre fichier CSV
csv_path = r'C:\Users\gchupe\flightPredict\dataset\rawData\flight_dataset.csv'

# Lire le fichier CSV
df = pd.read_csv(csv_path)

# Afficher les premières lignes
print(df.head())
