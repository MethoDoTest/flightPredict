import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from carbon_emission import calculate_training_emissions, calculate_inference_emissions, print_emission_comparison

# Charger le dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Séparer les données en train et test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de base (RandomForestClassifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Fonction d'inférence du modèle
def infer_model():
    predictions = model.predict(X_test)
    return predictions

# Tracker pour mesurer les émissions pendant l'entraînement
tracker = EmissionsTracker()
tracker.start()

# (Simuler) Lancer la fonction d'entraînement du modèle - Ici, on utilise un modèle pré-entraîné
# Donc, cette partie est commentée
# model.fit(X_train, y_train)

emissions_train = tracker.stop()
print(f"Emissions durant l'entraînement (simulée): {emissions_train} kg CO2eq")

# Tracker pour mesurer les émissions pendant l'inférence
tracker = EmissionsTracker()
tracker.start()

# Calcul des émissions durant l'inférence
emissions_infer = calculate_inference_emissions(infer_model)

# Affichage de la comparaison des émissions avec les kilomètres parcourus en voiture
print_emission_comparison(emissions_train, emissions_infer)
