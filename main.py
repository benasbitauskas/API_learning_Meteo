import requests
from pprint import pprint


base_url = 'https://api.meteo.lt/v1/stations/vilniaus-ams/observations/latest'


weather_data = requests.get(base_url).json()

pprint(weather_data)
