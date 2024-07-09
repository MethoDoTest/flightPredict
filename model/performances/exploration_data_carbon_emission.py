import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV
file_path = 'emissions.csv'
df = pd.read_csv(file_path)

# Convertir la colonne 'timestamp' en type datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Créer un graphique des émissions de CO2 au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['emissions'], marker='o', linestyle='-')
plt.xlabel('Timestamp')
plt.ylabel('Emissions (kg CO2eq)')
plt.title('Emissions de CO2 au fil du temps')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Afficher le graphique
plt.show()
