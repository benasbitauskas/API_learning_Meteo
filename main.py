import requests
from pprint import pprint
from datetime import date

# city = input("Įveskite miestą: ")
base_url = 'https://api.meteo.lt/v1/'
today = str(date.today())

station = ''


def show_forecast(city):
    forecast = base_url + 'places/' + city + '/forecasts/long-term'
    forecast = requests.get(forecast).json()
    pprint(forecast)
    data_forecast = forecast['forecastTimestamps'][0]['airTemperature']
    return data_forecast


def show_stations():
    stations = base_url + 'stations/'
    stations_info = requests.get(stations).json()
    return stations_info
    # TODO add stations info that it would show chosen station


def show_station_weather():
    stations_weather = base_url + 'stations/' + 'vilniaus-ams/observations/latest/'
    stations_weather = requests.get(stations_weather).json()
    stations_data = stations_weather['observations'][-1]['airTemperature']
    return stations_data


# print('1------------------------------------')
# show_forecast()
# print('2------------------------------------')
# show_stations()
# print('3------------------------------------')
# show_station_weather()
