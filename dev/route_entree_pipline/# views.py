# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import des nouvelles fonctions de traitement depuis le fichier processing.py
from processing.processing_fonction import (
    analyze_missing_values,
    impute_missing_values,
    generate_feature_report,
    create_new_features,
    is_holiday,
    encode_categorical_variables,
    preprocess_data,
)
#Le code est à corriger
@api_view(['POST'])
def data_pipeline(request):
    try:
        # Recevoir les données JSON du corps de la requête
        data = request.data

        # Convertir les données JSON en DataFrame
        df = pd.DataFrame(data)
        
        # Définir les colonnes catégorielles et la colonne cible
        colonnes_categorielles = ['Airline', 'Source', 'Destination']
        colonne_target = 'Price'  # Remplacez par la colonne cible de votre dataset

        # Prétraiter les données
        X, y = pretraiter_donnees(df, colonnes_categorielles, colonne_target)
        
        return Response({"message": "Données traitées avec succès", "features": X.head().to_dict(), "target": y.head().to_dict()}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
