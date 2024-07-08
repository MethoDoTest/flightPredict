import pytest
from django.urls import reverse
from unittest.mock import patch
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def url():
    return reverse("travel")


def test_travel_view_get(client, url):
    """Test that the travel view renders correctly on GET request."""
    response = client.get(url)
    assert response.status_code == 200
    assert "travel/travel_form.html" in [t.name for t in response.templates]
    assert "form" in response.context


@patch("travel.views.requests.post")
def test_travel_view_post_valid(mock_post, client, url):
    """Test that the travel view handles valid POST request."""
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"result": "Test Result"}

    data = {
        "airline": "Example Airline",
        "source": "CityA",
        "destination": "CityB",
        "total_stops": 1,
        "price": 200.5,
        "date": 15,
        "month": 7,
        "year": 2023,
        "dep_hours": 10,
        "dep_min": 30,
        "arrival_hours": 12,
        "arrival_min": 45,
        "duration_hours": 2,
        "duration_min": 15,
        "submit": "submit",
    }

    response = client.post(url, data)

    assert response.status_code == 200
    print("Reponse : ", response.context["form"])


def test_travel_view_post_invalid(client, url):
    """Test that the travel view handles invalid POST request."""
    data = {
        "airline": "",
        "source": "",
        "destination": "",
        "total_stops": 1,
        "price": 200.5,
        "date": 15,
        "month": 7,
        "year": 2023,
        "dep_hours": 10,
        "dep_min": 30,
        "arrival_hours": 12,
        "arrival_min": 45,
        "duration_hours": 2,
        "duration_min": 15,
        "submit": "submit",
    }

    headers = {"Content-Type": "application/json"}

    response = client.post(url, data, **headers)

    assert response.status_code == 200
    print("Fonction error : ", response.context["errors"])


def test_travel_view_post_clear(client, url):
    """Test that the travel view clears the form on POST request."""
    data = {"clear": "clear"}
    response = client.post(url, data)
    assert response.status_code == 200
    assert "form" in response.context
    assert not response.context["form"].is_bound
