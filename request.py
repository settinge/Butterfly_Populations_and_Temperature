import requests
import json
import datetime


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

start_dates = ['20201001','20201101','20201201','20210101','20210201','20210301']
end_dates = ['20201031','20201130','20201231','20210131','20210228','20210331']

def get_historical_weather_data(BASE_WEATHER_URL, weather_headers, start_dates, end_dates):
    for start_end in range(0,len(start_dates)):
        params['startDate'] = start_dates[start_end]
        params['endDate'] = end_dates[start_end]
        weather_data = requests.get(url = BASE_WEATHER_URL, headers = weather_headers, params = params)
        json_weather_data = weather_data.json()
        observation_data = json_weather_data.get('observations')
        date_conversion(observation_data)

def date_conversion(observation_data):
    for value in observation_data:
        weather_collection_date = datetime.datetime.fromtimestamp(value.get('valid_time_gmt'))
        weather_collection_hour = str(weather_collection_date).split(' ')[1]
        if weather_collection_hour == '14:54:00':
            print(weather_collection_date, value.get('temp'))
    
get_historical_weather_data(BASE_WEATHER_URL,weather_headers, start_dates, end_dates)