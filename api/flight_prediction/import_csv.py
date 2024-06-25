import os
import django
import csv

# Configurer Django pour utiliser les paramètres de votre projet
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_prediction.settings")
django.setup()

from api.models import FlightPrice

# Chemin vers le fichier CSV
file_path = r"dataset\rawData\flight_dataset.csv"


# Fonction pour importer les données CSV
def import_csv():
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            FlightPrice.objects.create(
                airline=row["Airline"],
                source=row["Source"],
                destination=row["Destination"],
                total_stops=int(row["Total_Stops"]),
                price=float(row["Price"]),
                date=int(row["Date"]),
                month=int(row["Month"]),
                year=int(row["Year"]),
                dep_hours=int(row["Dep_hours"]),
                dep_min=int(row["Dep_min"]),
                arrival_hours=int(row["Arrival_hours"]),
                arrival_min=int(row["Arrival_min"]),
                duration_hours=int(row["Duration_hours"]),
                duration_min=int(row["Duration_min"]),
            )
    print("Successfully loaded flight prices from CSV")


# Appel de la fonction d'importation
if __name__ == "__main__":
    import_csv()
