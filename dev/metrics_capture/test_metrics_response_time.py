# test_metrics_response_time.py
import pytest
import numpy as np
from metrics_reponse_time import (
    timed_mean_squared_error,
    timed_r2_score,
    timed_root_mean_squared_error,
    timed_mean_absolute_error,
)


class MockFlightPriceModel:
    def predict(self, X):
        # Simulate a prediction with some added noise
        return X + np.random.normal(0, 0.1, size=X.shape)


@pytest.fixture
def mock_model():
    return MockFlightPriceModel()


def test_timed_mean_squared_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    mse, time_taken = timed_mean_squared_error(mock_model, X, y_true)
    assert mse >= 0
    print(f"Mean Squared Error Time: {time_taken} seconds")


def test_timed_r2_score(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    r2, time_taken = timed_r2_score(mock_model, X, y_true)
    assert -1 <= r2 <= 1
    print(f"R2 Score Time: {time_taken} seconds")


def test_timed_root_mean_squared_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    rmse, time_taken = timed_root_mean_squared_error(mock_model, X, y_true)
    assert rmse >= 0
    print(f"Root Mean Squared Error Time: {time_taken} seconds")


def test_timed_mean_absolute_error(mock_model):
    X = np.array([200, 150, 300, 400])
    y_true = np.array([210, 160, 290, 390])
    mae, time_taken = timed_mean_absolute_error(mock_model, X, y_true)
    assert mae >= 0
    print(f"Mean Absolute Error Time: {time_taken} seconds")


if __name__ == "__main__":
    pytest.main()
