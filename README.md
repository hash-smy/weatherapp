# Weather App

This is a simple weather web application built using Python, Flask, HTML, CSS, and JavaScript. It allows users to retrieve weather information for both their current location and manually looked-up locations.

#Features
Current Location Weather: Fetches and displays weather details for the user's current location using geolocation.
Manual Lookup Weather: Allows users to input a city name manually and retrieve weather information for that specific location.
Display Weather Information: Displays weather details including temperature, weather description, humidity, sunrise, and sunset time.

#Prerequisites
Python 3.x installed
API key from OpenWeatgerMap
#Installation
Clone the repository:

'''
git clone https://github.com/hash-smy/weatherapp.git
'''

Install dependencies:

'''
pip install -r requirements.txt
'''

Set up your API key:

Obtain an API key from OpenWeatherMap.

Create a .env file in the project root directory.

Add your API key to the .env file:

'''
API_KEY=your_api_key_here
'''

Usage
Run the Flask application:

'''
python app.py
'''

Access the application in your web browser at http://localhost:5000.

Click on "Get Current Location Weather" to fetch weather details for your current location.

Alternatively, enter a city name in the "Manual Lookup Weather" section and click "Get Weather" to retrieve weather information for that city.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

