import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

from train import train

df = pd.DataFrame({
    'Airline': [1],
    'Source': [1],
    'Destination': [1],
    'Total_Stops': [1],
    'Date': [1],
    'Month': [1],
    'Year': [2020],
    'Dep_hours': [10],
    'Dep_min': [30],
    'Arrival_hours': [12],
    'Arrival_min': [45],
    'Duration_hours': [2],
    'Duration_min': [15]
})
target = pd.Series(100)


def test_train_model_not_allowed(data_x=df, data_y=target, model="test"):
    with pytest.raises(TypeError):
        train.train_model(data_x=data_x, data_y=data_y, model=model)


def test_train_return_model(data_x=df, data_y=target, model=LinearRegression()):
    assert isinstance(train.train_model(data_x=data_x, data_y=data_y, model=model), type(model))
