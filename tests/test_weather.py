import unittest
from unittest.mock import MagicMock
from app.weather import WeatherAPI

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.weather_api = WeatherAPI()

    def test_get_weather_success(self):
        mock_response = {
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
            "main": {"temp": 16.18, "humidity": 72},
            "name": "San Francisco",
        }
        
        self.weather_api.get_weather = MagicMock(return_value=mock_response)
        city = "San Francisco"
        weather_data = self.weather_api.get_weather(city)
        self.assertEqual(weather_data["name"], city)
        self.assertEqual(weather_data["weather"][0]["main"], "Clear")

    def test_get_weather_failure(self):
        self.weather_api.get_weather = MagicMock(return_value=None)
        city = "Invalid City"
        weather_data = self.weather_api.get_weather(city)
        self.assertIsNone(weather_data)

    def test_get_weather_by_coordinates_success(self):
        mock_response = {
            "coord": {"lon": -122.08, "lat": 37.39},
            "weather": [{"id": 800, "main": "Clear", "description": "clear sky"}],
            "main": {"temp": 16.18, "humidity": 72},
            "name": "San Francisco",
        }
        
        self.weather_api.get_weather_by_coordinates = MagicMock(return_value=mock_response)
        
        latitude = 37.39
        longitude = -122.08
        weather_data = self.weather_api.get_weather_by_coordinates(latitude, longitude)
        self.assertEqual(weather_data["name"], "San Francisco")
        self.assertEqual(weather_data["weather"][0]["main"], "Clear")

    def test_get_weather_by_coordinates_failure(self):
        self.weather_api.get_weather_by_coordinates = MagicMock(return_value=None)
        latitude = 100.0  
        longitude = 200.0  
        weather_data = self.weather_api.get_weather_by_coordinates(latitude, longitude)
        self.assertIsNone(weather_data)

if __name__ == "__main__":
    unittest.main()
