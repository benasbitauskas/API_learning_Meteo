import requests
from pprint import pprint
from datetime import date

# city = input("Įveskite miestą: ")
base_url = 'https://api.meteo.lt/v1/'
today = str(date.today())
stations = base_url + 'stations/'
forecast = base_url + 'places/' + 'Kaunas' + '/forecasts/long-term'
forecast = requests.get(forecast).json()['airTemperature']

# for key in list(forecast.keys()):
#     if key == 'airTemperature':
pprint(forecast)
