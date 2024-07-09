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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de base (RandomForestClassifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fonction d'inférence du modèle
def infer_model():
    predictions = model.predict(X_test)
    return predictions

# Tracker pour mesurer les émissions pendant l'entraînement (simulation)
def train_model_simulation():
    # Simulation de l'entraînement, car le modèle est déjà entraîné
    pass

# Calcul des émissions durant l'entraînement (simulation)
emissions_train = calculate_training_emissions(train_model_simulation)

# Calcul des émissions durant l'inférence
emissions_infer = calculate_inference_emissions(infer_model)

# Affichage de la comparaison des émissions avec les kilomètres parcourus en voiture
print_emission_comparison(emissions_train, emissions_infer)
