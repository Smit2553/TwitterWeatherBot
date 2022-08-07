import requests
from dotenv import load_dotenv
import os
from weather import *


def twitterpost(data=get_weather_data()):
    temperature_k = data['main']['temp']
    temperature_c = temperature_k - 273.15
    temperature_f = 1.8 * (temperature_k - 273) + 32
    general_weather = data['weather'][0]['description']
