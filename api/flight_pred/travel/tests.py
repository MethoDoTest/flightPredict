from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch


class TravelViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse(
            "travel"
        )  # Assurez-vous que 'travel_view' correspond au nom de votre URL

    def test_travel_view_get(self):
        """Test that the travel view renders correctly on GET request."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "travel/travel_form.html")
        self.assertIn("form", response.context)

    @patch("travel.views.requests.post")
    def test_travel_view_post_valid(self, mock_post):
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

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)
        print("Reponse : ", response.context["form"])

    #  self.assertIn("result", response.context["result"])
    # self.assertEqual(response.context["result"], "Test Result")

    def test_travel_view_post_invalid(self):
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

        response = self.client.post(self.url, data, headers=headers)

        self.assertEqual(response.status_code, 200)
        print("Fonction error : ", response.context["errors"])

    # self.assertIn("errors", response.context)
    # self.assertTrue(response.context["errors"])

    def test_travel_view_post_clear(self):
        """Test that the travel view clears the form on POST request."""
        data = {"clear": "clear"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertFalse(response.context["form"].is_bound)


if __name__ == "__main__":
    TravelViewTests().test_travel_view_get()
    TravelViewTests().test_travel_view_post_valid()
    TravelViewTests().test_travel_view_post_invalid()
    TravelViewTests().test_travel_view_post_clear()
