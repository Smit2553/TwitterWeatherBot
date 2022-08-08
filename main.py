from weather import *
import tweepy
import urllib.parse
import time


def twitterpost():
    city = get_city()
    data = get_weather_data(city)
    temperature_k = data['main']['temp']
    temperature_c = round((temperature_k - 273.15), 2)
    temperature_f = round((1.8 * (temperature_k - 273) + 32), 2)
    general_weather = data['weather'][0]['description']
    consumer_key = os.environ.get('CONSUMERKEY')
    consumer_secret = os.environ.get('CONSUMERSECRET')
    access_token = os.environ.get('ACCESSTOKEN')
    access_token_secret = os.environ.get('ACCESSTOKENSECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    googlemapslink = urllib.parse.quote(f'{city[0]}')

    api.update_status(status=f"""
    Location = {city[0]}, {city[1]}
    Celcius = {temperature_c} C
    Fahrenheit = {temperature_f} F
    Conditions = {general_weather}
    https://www.google.com/maps/search/?api=1&query={googlemapslink}  #weather #city #{city[0]}""")
    print(f'Location = {city[0]}, {city[1]}')


while True:
    twitterpost()
    time.sleep(3600)
