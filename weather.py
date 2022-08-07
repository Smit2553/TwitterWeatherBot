import requests
from dotenv import load_dotenv
import os
from city import *

load_dotenv()


def get_weather_data(city=None):
    if city is None:
        city = get_city()

    weatherapikey = os.environ.get("WEATHERAPI")
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city[0]}&APPID={weatherapikey}').json()
    return response



