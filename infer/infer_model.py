import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, RANSACRegressor


def load_model(model_path):
    """
        Function to load a joblib model
        -------------
        Inputs
        -------------
        @params model_path string: path of the model we want to load

        -------------
        Return
        -------------
        model : joblib model
    """
    model = joblib.load(model_path)
    return model


def infer_model(model, data):
    """
        Function to get inference from model
        -------------
        Inputs
        -------------
        @params data pandas.DataFrame: dataset, in pandas dataframe format
        @params model : loaded model

        -------------
        Return
        -------------
        prediction of the price
    """
    return model.predict(data)
