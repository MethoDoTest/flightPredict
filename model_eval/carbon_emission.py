from codecarbon import EmissionsTracker

# 1 Tracker pour mesurer les émissions pendant l'entraînement
tracker = EmissionsTracker()
tracker.start()

#Lancer la fonction d'entrainement du model exemple : train_model()

emissions_train = tracker.stop()
print(f"Emissions durant l'entraînement: {emissions_train} kg CO2eq")

# 2 Tracker pour mesurer les émissions pendant l'inférence
tracker = EmissionsTracker()
tracker.start()

#Lancer la fonction d'inference du model exemple : train_model()

emissions_infer = tracker.stop()
print(f"Emissions durant l'inférence: {emissions_infer} kg CO2eq")

# 3 Comparaison avec les émissions d'une voiture
# En moyenne, une voiture émet environ 0.12 kg de CO2 par kilomètre parcouru
emissions_per_km = 0.12

km_train = emissions_train / emissions_per_km
km_infer = emissions_infer / emissions_per_km

print(f"Les émissions durant l'entraînement sont équivalentes à {km_train:.2f} km parcourus en voiture.")
print(f"Les émissions durant l'inférence sont équivalentes à {km_infer:.2f} km parcourus en voiture.")