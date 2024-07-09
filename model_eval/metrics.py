# metrics.py
import numpy as np


def mean_squared_error(model, X, y_true):
    """
    Calculate Mean Squared Error (MSE)
    """
    y_pred = model.predict(X)
    return np.mean((y_true - y_pred) ** 2)


def r2_score(model, X, y_true):
    """
    Calculate R^2 (Coefficient of Determination)
    """
    y_pred = model.predict(X)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)


def root_mean_squared_error(model, X, y_true):
    """
    Calculate Root Mean Squared Error (RMSE)
    """
    mse = mean_squared_error(model, X, y_true)
    return np.sqrt(mse)


def mean_absolute_error(model, X, y_true):
    """
    Calculate Mean Absolute Error (MAE)
    """
    y_pred = model.predict(X)
    return np.mean(np.abs(y_true - y_pred))
