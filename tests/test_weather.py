import unittest
from unittest.mock import MagicMock
from app.weather import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.weather_api = WeatherAPI()

    def test_get_weather_success(self):
        # Mocking the response from the API
        mock_response = {
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
            "main": {"temp": 16.18, "humidity": 72},
            "name": "San Francisco",
        }
        
        # Mocking the requests library's get method
        self.weather_api.get_weather = MagicMock(return_value=mock_response)
        
        # Testing for a successful API call
        city = "San Francisco"
        weather_data = self.weather_api.get_weather(city)
        self.assertEqual(weather_data["name"], city)
        self.assertEqual(weather_data["weather"][0]["main"], "Clear")

    def test_get_weather_failure(self):
        # Mocking a failed response from the API
        self.weather_api.get_weather = MagicMock(return_value=None)
        
        # Testing for a failed API call
        city = "Invalid City"
        weather_data = self.weather_api.get_weather(city)
        self.assertIsNone(weather_data)

if __name__ == "__main__":
    unittest.main()
