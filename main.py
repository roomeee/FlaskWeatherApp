from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_weatherdata():
    if request.method == 'POST':
        city = request.form['city']
        EndPoint = "https://api.openweathermap.org/data/2.5/weather"
        api_key = "b076307ad8f0e78d8ff00e58e562d43c"
        weather_params = {
            "q": city,
            "appid": api_key,
            "units": "metric",
        }
        response = requests.get(EndPoint, params=weather_params)
        response.raise_for_status()
        data = response.json()

        weather_details = {
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Pressure": f"{data['main']['pressure']} hPa",
            "Wind Speed": f"{data['wind']['speed']} m/s",
            "Weather": data['weather'][0]['description'],
        }

        return render_template('index.html', weather_details=weather_details)

    return render_template('index.html', weather_details=None)

app.run(host='0.0.0.0',debug=False)
