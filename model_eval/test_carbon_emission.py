import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from codecarbon import EmissionsTracker

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
def infer_model(model, X_test):
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

# Lancer la fonction d'inférence du modèle
predictions = infer_model(model, X_test)

emissions_infer = tracker.stop()
print(f"Emissions durant l'inférence: {emissions_infer} kg CO2eq")

# Comparaison avec les émissions d'une voiture
# En moyenne, une voiture émet environ 0.12 kg de CO2 par kilomètre parcouru
emissions_per_km = 0.12

km_train = emissions_train / emissions_per_km
km_infer = emissions_infer / emissions_per_km

print(f"Les émissions durant l'entraînement (simulée) sont équivalentes à {km_train:.2f} km parcourus en voiture.")
print(f"Les émissions durant l'inférence sont équivalentes à {km_infer:.2f} km parcourus en voiture.")
