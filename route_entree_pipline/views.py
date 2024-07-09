from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

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

        # Analyser les valeurs manquantes
        missing_values_report = analyze_missing_values(df)

        # Imputer les valeurs manquantes
        df = impute_missing_values(df)

        # Générer un rapport sur les fonctionnalités
        feature_report = generate_feature_report(df)

        # Créer de nouvelles fonctionnalités
        df = create_new_features(df)

        # Encoder les variables catégorielles
        df = encode_categorical_variables(df, colonnes_categorielles)

        # Prétraiter les données
        X, y = preprocess_data(df, colonne_target)

        return Response({
            "message": "Données traitées avec succès",
            "features": X.head().to_dict(),
            "target": y.head().to_dict(),
            "missing_values_report": missing_values_report,
            "feature_report": feature_report
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
