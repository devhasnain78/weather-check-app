import requests
import random

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "4e03a061f29c7514507d7c5f54325dab"

params = {
    # "lat": random.uniform(-90.0, 90.0),
    # "lon" : random.uniform(-180.0, 180.0),
    "lat": 50.517636,
    "lon": 1.827528,
    "appid":API_KEY,
    "cnt":3
}

response = requests.get(OWM_ENDPOINT,params )
response.raise_for_status()

data = response.json()["list"]

will_rain = False

for items in data:
    weather_data = items["weather"]
    weather_id = weather_data[0]["id"]
    if weather_id<700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

print(response.status_code)