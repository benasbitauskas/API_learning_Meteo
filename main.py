import requests
from pprint import pprint
from datetime import date

# city = input("Įveskite miestą: ")
base_url = 'https://api.meteo.lt/v1/'
today = str(date.today())
stations = base_url + 'stations/' + 'vilniaus-ams/observations/latest'
stations = requests.get(stations).json()
stations_data = stations['observations'][-1]['airTemperature']

pprint(stations)
pprint(stations_data)

# forecast = base_url + 'places/' + 'Vilnius' + '/forecasts/long-term'
# forecast = requests.get(forecast).json()
# pprint(forecast)
# data_forecast = forecast['forecastTimestamps'][0]['airTemperature']
# pprint(data_forecast)
