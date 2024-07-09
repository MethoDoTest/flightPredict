from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

# Import des nouvelles fonctions de traitement depuis le fichier processing.py
from processing.processing_fonction import (
    generate_feature_report,
    create_new_features,
    encode_categorical_variables,
    preprocess_data,
    analyze_missing_values,
    impute_missing_values,
)

@api_view(['POST'])
def data_pipeline(request):
    try:
        # Recevoir les données JSON du corps de la requête
        #data = request.data

        # Convertir les données JSON en DataFrame
       # df = pd.DataFrame(data)
        df = request.data

        # Définir les colonnes catégorielles et la colonne cible
        colonnes_categorielles = ['Airline', 'Source', 'Destination']

        # Générer un rapport sur les fonctionnalités
        feature_report = generate_feature_report(df)

        # Créer de nouvelles fonctionnalités
        df = create_new_features(df)

        # Encoder les variables catégorielles
        df = encode_categorical_variables(df)

        # Prétraiter les données
        df = preprocess_data(df)
            return df
        # Analyser les valeurs manquantes
        missing_values_report = analyze_missing_values(df)

        # Imputer les valeurs manquantes
        df = impute_missing_values(df)
        
        return Response({
            "message": "Données traitées avec succès",
            "features": X.head().to_dict(),
            "target": y.head().to_dict(),
            "missing_values_report": missing_values_report,
            "feature_report": feature_report
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
