# Random City Twitter Bot

## This bot posts hourly on https://twitter.com/RCityWeather

### To help develop kindly make a Pull Request.

#### This twitter bot picks a random city from around the globe every hour and posts its weather information as a tweet.

To install this repo locally run the following commands:
```bash
git clone https://github.com/Smit2553/TwitterWeatherBot.git

cd TwitterWeatherBot

pip install -r requirements.txt
```

Go to https://openweathermap.org/ and create an API key.

Create a Twitter Developer account at https://developer.twitter.com

Create a .env file in the TwitterWeatherBot directory with the following keys:

```
WEATHERAPI=
CONSUMERKEY=
CONSUMERSECRET=
ACCESSTOKEN=
ACCESSTOKENSECRET=
```

Finally, you can run:

```
python3 main.py
```