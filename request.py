import requests
import json
import datetime
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

start_dates = ['20201001','20201101','20201201','20210101','20210201','20210301','20210401','20210501','20210601','20210701','20210801','20210901','20211001','20211101','20211201','20220101']
end_dates = ['20201031','20201130','20201231','20210131','20210228','20210331','20210430','20210531','20210630','20210731','20210831','20210930','20211031','20211130','20211231','20220131']

temperature_list = []

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
            temperature_list.append({'Date':str(weather_collection_date).split(' ')[0],'Temp':value.get('temp')})
    write_data_to_json(temperature_list)
         
def write_data_to_json(temperature_list):
    with open(os.path.join("C:\\Users\\swimm\\OneDrive\\Desktop\\Butterfly_Repo\\Butterfly_Populations_and_Temperature\\data","temp_data.json"), "w") as temp_data_file:
        temp_data_file.write(json.dumps(temperature_list))

get_historical_weather_data(BASE_WEATHER_URL,weather_headers, start_dates, end_dates)