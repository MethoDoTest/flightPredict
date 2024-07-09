import time
import numpy as np
from metrics import (
    mean_squared_error,
    r2_score,
    root_mean_squared_error,
    mean_absolute_error,
)


def timed_mean_squared_error(model, X, y_true):
    start_time = time.time()
    mse = mean_squared_error(model, X, y_true)
    end_time = time.time()
    return mse, end_time - start_time


def timed_r2_score(model, X, y_true):
    start_time = time.time()
    r2 = r2_score(model, X, y_true)
    end_time = time.time()
    return r2, end_time - start_time


def timed_root_mean_squared_error(model, X, y_true):
    start_time = time.time()
    rmse = root_mean_squared_error(model, X, y_true)
    end_time = time.time()
    return rmse, end_time - start_time


def timed_mean_absolute_error(model, X, y_true):
    start_time = time.time()
    mae = mean_absolute_error(model, X, y_true)
    end_time = time.time()
    return mae, end_time - start_time
