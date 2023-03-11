import requests
from pprint import pprint
from datetime import date

base_url = 'https://api.meteo.lt/v1/'
today = str(date.today())
stations = base_url + 'stations/'
# weather_info = stations+station_code+'/observations/'+today
places = base_url + 'places/'

places = requests.get(places).json()

pprint(places)
