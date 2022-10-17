import requests
import json
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import os
import calendar

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

start_date = ['19961001','19970201']
end_date = ['20211001', '20220201']

actual_start_date_string = start_date[0]
actual_start_date_date = datetime.strptime(start_date[0], '%Y%m%d')
actual_end_date = datetime.strptime(start_date[1], '%Y%m%d')
end_date_start_date = datetime.strptime(start_date[0], '%Y%m%d') + timedelta(days=30)
end_date_start_string = datetime.strftime(end_date_start_date,'%Y%m%d')
temperature_list = []
num_years = 2022-1996
counter = 0

def get_historical_weather_data(BASE_WEATHER_URL,weather_headers,actual_start_date_string, actual_start_date_date, actual_end_date, end_date_start_string, end_date_start_date):
    num_months = (actual_end_date.year - actual_start_date_date.year) * 12 + (actual_end_date.month - actual_start_date_date.month) + 1
    years_months = num_years * num_months
    for timeinterval in range(0,years_months):
        params['startDate'] = actual_start_date_string
        params['endDate'] = end_date_start_string
        weather_data = requests.get(url = BASE_WEATHER_URL, headers = weather_headers, params = params)
        json_weather_data = weather_data.json()
        observation_data = json_weather_data.get('observations')
        
        if actual_start_date_date.month == 3:
            actual_start_date_date = actual_start_date_date + relativedelta(months=+7)
        else:
            actual_start_date_date = actual_start_date_date + relativedelta(months=1)
        actual_start_date_string = datetime.strftime(actual_start_date_date,'%Y%m%d')

        if actual_start_date_string[4] == 0:
            month_parameter = actual_start_date_string[5]
        else:
            month_parameter = actual_start_date_string[4:6]
        year_parameter = actual_start_date_string[0:4]

        last_month_day = calendar.monthrange(int(year_parameter), int(month_parameter))
        end_date_start_string = f'{year_parameter}{actual_start_date_string[4:6]}{last_month_day[1]}'
        if observation_data:
            date_conversion(observation_data)
        else:
            raise Exception("No data for the specified range")

def date_conversion(observation_data):
    for value in observation_data:
        weather_collection_date = datetime.fromtimestamp(value.get('valid_time_gmt'))
        weather_collection_hour = str(weather_collection_date).split(' ')[1]
        weather_collection_day = str(weather_collection_date).split('-')[2][:2]
        if weather_collection_hour == '14:54:00' and weather_collection_day == '15':
            temperature_list.append({'Date':str(weather_collection_date).split(' ')[0],'Temp':value.get('temp')})
    write_data_to_json(temperature_list)
         
def write_data_to_json(temperature_list):
    with open(os.path.join("C:\\Users\\swimm\\OneDrive\\Desktop\\Butterfly_Repo\\Butterfly_Populations_and_Temperature\\data","temp_data.json"), "w") as temp_data_file:
        temp_data_file.write(json.dumps(temperature_list))

get_historical_weather_data(BASE_WEATHER_URL,weather_headers,actual_start_date_string, actual_start_date_date, actual_end_date, end_date_start_string, end_date_start_date)