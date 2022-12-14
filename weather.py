import requests
from dotenv import load_dotenv
import os
from city import *

load_dotenv()


def get_weather_data(city):
    weatherapikey = os.environ.get("WEATHERAPI")
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city[0]},{city[1]}&APPID={weatherapikey}').json()
    return response



