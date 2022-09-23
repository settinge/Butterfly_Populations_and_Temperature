import pandas as pd
import json
import os

butterfly_path = ['total_butterfly_data.xlsx']
start_year = 1997
end_year = 2022
county = 'Monterey'
total_bfly_data = []

def read_butterfly_data(excel_name, sheet):
    for file in range(0,len(excel_name)):
        df = pd.read_excel(excel_name[file], sheet)
    get_and_select_columns(df,start_year,end_year)

def get_and_select_columns(df, start_year, end_year):
    for year in range(start_year, end_year):
        df = df.loc[(df['COUNTY']=='Monterey') & 
        (df['SITE NAME'] == 'Butterfly Grove Sanctuary,  Pacific Grove')]
        sub_df = df.loc[:,year]
        year_value = sub_df.iloc[0]
        write_json_data(year, year_value)

def write_json_data(year, year_value):
    total_bfly_data.extend([{year:int(year_value)}])
    cwd = os.getcwd()
    filepath = os.path.join(cwd, 'data')
    with open(os.path.join(filepath, "total_butterfly_data.json"),"w") as all_bfly_data:
        all_bfly_data.write(json.dumps(total_bfly_data))

read_butterfly_data(butterfly_path, 0)