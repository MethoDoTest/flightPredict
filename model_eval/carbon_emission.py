from codecarbon import EmissionsTracker
 
def calculate_training_emissions(train_function):
    """
    Calcule les émissions de CO2 durant l'entraînement du modèle.
    
    Args:
        train_function (callable): La fonction d'entraînement du modèle.
    
    Returns:
        float: Les émissions de CO2 en kg équivalent.
    """
    tracker = EmissionsTracker()
    tracker.start()
    train_function()
    emissions_train = tracker.stop()
    print(f"Emissions durant l'entraînement: {emissions_train} kg CO2eq")
    return emissions_train

def calculate_inference_emissions(inference_function):
    """
    Calcule les émissions de CO2 durant l'inférence du modèle.
    
    Args:
        inference_function (callable): La fonction d'inférence du modèle.
    
    Returns:
        float: Les émissions de CO2 en kg équivalent.
    """
    tracker = EmissionsTracker()
    tracker.start()
    inference_function()
    emissions_infer = tracker.stop()
    print(f"Emissions durant l'inférence: {emissions_infer} kg CO2eq")
    return emissions_infer

def compare_emissions_to_car(emissions):
    """
    Compare les émissions de CO2 à des kilomètres parcourus en voiture.
    
    Args:
        emissions (float): Les émissions de CO2 en kg équivalent.
    
    Returns:
        float: Les kilomètres parcourus équivalents.
    """
    emissions_per_km = 0.12  # kg CO2 par kilomètre
    km_equivalent = emissions / emissions_per_km
    return km_equivalent

def print_emission_comparison(emissions_train, emissions_infer):
    """
    Affiche la comparaison des émissions avec des kilomètres parcourus en voiture.
    
    Args:
        emissions_train (float): Les émissions durant l'entraînement en kg CO2eq.
        emissions_infer (float): Les émissions durant l'inférence en kg CO2eq.
    """
    km_train = compare_emissions_to_car(emissions_train)
    km_infer = compare_emissions_to_car(emissions_infer)
    print(f"Les émissions durant l'entraînement sont équivalentes à {km_train:.2f} km parcourus en voiture.")
    print(f"Les émissions durant l'inférence sont équivalentes à {km_infer:.2f} km parcourus en voiture.")
