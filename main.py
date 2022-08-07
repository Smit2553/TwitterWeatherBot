import requests
from dotenv import load_dotenv
import os
import json

city = 'London'
weatherapikey = os.environ.get("WEATHERAPI")
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={weatherapikey}')



load_dotenv()
print(os.environ[""])