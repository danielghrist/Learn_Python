import requests
from datetime import datetime
import time

MY_LAT = 29.615860  # Your latitude
MY_LONG = -98.599720  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


# Check if ISS is within 5 degrees of your position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS Latitude:  {iss_latitude}")
    print(f"ISS Longitude:  {iss_longitude}")

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    """This API returns the UTC format of time and this code won't work correctly\n 
        API does not account for time zone so need to set the UTC - 6 Central Time Offset\n
        Code may not correctly calculate offset when time is less than 6 AM UTC"""
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data) # For Testing
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 6
    print(f"Today's Sunrise:  {sunrise}")
    print(f"Today's Sunset:  {sunset}")

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    print(f"Is it currently dark: {is_dark()}\n")  # For Testing
    # If the ISS is close to my current position
    # and it is currently dark
    if is_iss_overhead() and is_dark():
        print("Look UP!\n")
    else:
        print("ISS hates you...\n")

    # BONUS: run the code every 60 seconds.
    time.sleep(60)

# Then send me an email to tell me to look up.
