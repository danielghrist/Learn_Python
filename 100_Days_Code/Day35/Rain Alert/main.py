import requests
import json
from datetime import datetime
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 29.615860
MY_LON = -98.599716
API_KEY = "257e8124c5c40b3494e3de679fa1d0e1"
# API_KEY = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
# Prints the HTTP status code, 200 for success
# print(response)
weather_data = response.json()

# Using Slicing to obtain only the next 12 hours of data
next_12_hours = weather_data["hourly"][:12]

# Using Dictionary Comprehension to create a new dictionary which contains the hour: idcode as key value pairs
weather_condition = {n: next_12_hours[n]["weather"][0]["id"] for n in range(len(next_12_hours))
                     if next_12_hours[n]["weather"][0]["id"] < 700}

# print(weather_condition)

# Determine what hours it will rain
current_hour = datetime.now().hour

if len(weather_condition) > 0:
    for hour, idcode in weather_condition.items():
        display_hour = hour + current_hour
        if display_hour >= 24:
            display_hour = 0 + hour
        print(f"{display_hour:02}:00 has a chance of rain that hour")
else:
    print("Looks like its all clear for the next 12 hours.")

# ***TEST STUFF I WAS PLAYING AROUND WITH***
# print(json.dumps(next_12_hours, indent=4))
# pretty_string = json.dumps(next_48_hours, indent=4)
# print(pretty_string)
