import requests
import json
from datetime import datetime, timedelta
import os

BASE_WEATHER_URL = 'https://api.weather.com/v1/location/KMRY:9:US/observations/historical.json?'

weather_headers = {'Accept': 'application/json, text/plain, */*',
'Referer': 'https://www.wunderground.com/',
'sec-ch-ua': 'Chromium;v=104, Not A;Brand;v=99, Google Chrome;v=104',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36}'}

params = {'apiKey': 'e1f10a1e78da46f5b10a1e78da96f525',
'units': 'e',
'startDate': '20201101',
'endDate': '20201130'}

start_date = ['20201001','20220201']
actual_start_date = datetime.strptime(start_date[0], '%Y%m%d')
actual_end_date = datetime.strptime(start_date[1], '%Y%m%d')
end_date_start = datetime.strptime(start_date[0], '%Y%m%d') + timedelta(days=30)
temperature_list = []

def get_historical_weather_data(BASE_WEATHER_URL, weather_headers, actual_start_date, actual_end_date, end_date_start):
    num_months = (actual_end_date.year - actual_start_date.year) * 12 + (actual_end_date.month - actual_start_date.month)
    for timeinterval in range(0,num_months):
        start_date_request = datetime.strftime(actual_start_date,'%Y%m%d')
        end_date_request = datetime.strftime(end_date_start,'%Y%m%d')
        params['startDate'] = start_date_request
        params['endDate'] = end_date_request
        weather_data = requests.get(url = BASE_WEATHER_URL, headers = weather_headers, params = params)
        json_weather_data = weather_data.json()
        observation_data = json_weather_data.get('observations')
        actual_start_date = actual_start_date + timedelta(days=31)
        end_date_start = end_date_start + timedelta(days=30)
        date_conversion(observation_data)
   
def date_conversion(observation_data):
    for value in observation_data:
        weather_collection_date = datetime.fromtimestamp(value.get('valid_time_gmt'))
        weather_collection_hour = str(weather_collection_date).split(' ')[1]
        if weather_collection_hour == '14:54:00':
            temperature_list.append({'Date':str(weather_collection_date).split(' ')[0],'Temp':value.get('temp')})
    write_data_to_json(temperature_list)
         
def write_data_to_json(temperature_list):
    with open(os.path.join("C:\\Users\\swimm\\OneDrive\\Desktop\\Butterfly_Repo\\Butterfly_Populations_and_Temperature\\data","temp_data.json"), "w") as temp_data_file:
        temp_data_file.write(json.dumps(temperature_list))

get_historical_weather_data(BASE_WEATHER_URL,weather_headers, actual_start_date, actual_end_date, end_date_start)