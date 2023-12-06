from flask import Flask, jsonify, request, render_template
from app.weather import WeatherAPI

app = Flask(__name__) 
weather_api = WeatherAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    if city:
        weather_data = weather_api.get_weather(city)
    elif latitude and longitude:
        weather_data = weather_api.get_weather_by_coordinates(latitude, longitude)
    else:
        return jsonify({"error": "Invalid request"}), 400
    
    if not weather_data:
        return jsonify({"error": "Failed to fetch weather data"}), 500
    
    return jsonify(weather_data)

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)



if __name__ == '__main__':
    app.run(debug=True)
