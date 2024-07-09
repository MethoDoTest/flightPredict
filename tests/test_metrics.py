# test_metrics.py
import pytest
import numpy as np
from model_eval.metrics import (
    mean_squared_error,
    r2_score,
    root_mean_squared_error,
    mean_absolute_error,
)


class MockFlightPriceModel:
    def predict(self, X):
        # Simulate a prediction with some added noise
        return X + np.random.normal(0, 0.1, size=X.shape)


@pytest.fixture
def mock_model():
    return MockFlightPriceModel()


def test_mean_squared_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    mse = mean_squared_error(mock_model, X, y_true)
    assert mse >= 0


def test_r2_score(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    r2 = r2_score(mock_model, X, y_true)
    assert -1 <= r2 <= 1


def test_root_mean_squared_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    rmse = root_mean_squared_error(mock_model, X, y_true)
    assert rmse >= 0


def test_mean_absolute_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    mae = mean_absolute_error(mock_model, X, y_true)
    assert mae >= 0


if __name__ == "__main__":
    pytest.main()
