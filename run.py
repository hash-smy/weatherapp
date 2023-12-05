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
    if not city:
        return jsonify({"error": "City parameter is missing"}), 400
    
    weather_data = weather_api.get_weather(city)
    if not weather_data:
        return jsonify({"error": "Failed to fetch weather data"}), 500
    
    return jsonify(weather_data)

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True)
