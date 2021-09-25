import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")
API_URL = "https://api.weatherapi.com/v1/current.json?key={}&q=London&aqi=no".format(API_KEY)

def get_current(city):
    params = "&q={}&aqi=no".format(city)

    response = requests.get(API_URL+params)
    print(response.content)

get_current("london")
