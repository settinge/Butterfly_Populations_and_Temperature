import pandas as pd
import json

butterfly_paths = ["C:\\Users\\swimm\\Downloads\\WMNYC_data_02.17.21.xlsx","C:\\Users\\swimm\\Downloads\\NewYearsData_2021-22.xlsx"]
butterfly_columns = ['WMTC 2020','WMNYC 2020/21','Thanksgiving Count 2021','New Year\'s Count 2021-22']
butterfly_count_list = []

def open_butterfly_excel(excel_name, sheet, columns):
    for file in range(0,len(excel_name)):
        df = pd.read_excel(excel_name[file], sheet)
        select_columns_and_munge(df, file, columns)
    
def select_columns_and_munge(df,file, columns):
    if file % 2 == 0 or file == 0:
        step_start = file
        step_end = file + 2
    else:
        step_start = file + 1
        step_end = file + 3

    column_selection = columns[step_start:step_end]
    if file == 1:
        new_header = df.iloc[0]
        df = df[1:]
        df.columns = new_header
    df = df.loc[df['COUNTY']=='Monterey']
    df_selected_columns = df[column_selection]
    df_selected_columns = df_selected_columns.fillna(0)
    sum_data_and_write(df_selected_columns, column_selection)

def sum_data_and_write(df_selected_columns, column_selection):
    total_thanksgiving_count = int(df_selected_columns[column_selection[0]].sum())
    total_new_years_count = int(df_selected_columns[column_selection[1]].sum())
    print(f'Thanksgiving count is {total_thanksgiving_count}')
    print(f'New Years count is {total_new_years_count}')
    butterfly_count_list.extend([{column_selection[0]:total_thanksgiving_count},
                                {column_selection[1]:total_new_years_count}])
    print(butterfly_count_list)
    with open('butterfly_data.json','w') as butterfly_data_file:
        butterfly_data_file.write(json.dumps(butterfly_count_list))

open_butterfly_excel(butterfly_paths, 0, butterfly_columns)