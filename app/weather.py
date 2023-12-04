import requests
import os
from dotenv import load_dotenv

load_dotenv()


class WeatherAPI:
    def get_weather(self, city):

        api_key = os.getenv("API_KEY")
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None