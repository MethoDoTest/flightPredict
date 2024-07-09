# prediction_model.py
import joblib
import numpy as np
import os


def load_model():
    """
    Load the pre-trained model from the file system
    """
    model_path = os.path.join(os.path.dirname(__file__), "model.sav")
    return joblib.load(model_path)


def predict_flight_price(
    model,
    departure,
    destination,
    airline,
    total_stops,
    date,
    month,
    year,
    dep_hours,
    dep_min,
    arrival_hours,
    arrival_min,
    duration_hours,
    duration_min,
):
    """
    Predict flight price using the pre-trained model
    """
    # Convert input data to the appropriate format for the model
    input_data = np.array(
        [
            [
                departure,
                destination,
                airline,
                total_stops,
                date,
                month,
                year,
                dep_hours,
                dep_min,
                arrival_hours,
                arrival_min,
                duration_hours,
                duration_min,
            ]
        ]
    )

    # Perform prediction
    return model.predict(input_data)[0]
