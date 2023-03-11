import requests
from pprint import pprint


base_url = 'https://api.meteo.lt/v1/stations/'


stations = requests.get(base_url).json()

pprint(stations)
