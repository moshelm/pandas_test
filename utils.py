import pandas as pd
from pandas import DataFrame

def load_json(json_file):
    df = pd.read_json(json_file)
    return df

def clean_numbers(df:DataFrame,name_column):
        df[name_column] = df[name_column].apply(lambda number:number if '$' not in number else number.replace('$',''))
        df[name_column] = pd.to_numeric(df[name_column])
        return df

def convert_to_datetime(df:DataFrame,name_column):
    df[name_column] = pd.to_datetime(df[name_column])
    return df

def remove_html_tags(df:DataFrame, name_column):
    df[name_column] = df[name_column].str.replace(r'<[^<>]*>', ' ', regex=True)
    return df

def replacing_empty_value(df:DataFrame,name_column):
    df[name_column] = df[name_column].apply(lambda x: x if x else 'no coupon')

def create_column_order_month(df:DataFrame, date_column,new_column):
    df['date'] = pd.to_datetime(df[date_column]).dt.date
    df[new_column] = pd.to_datetime(df['date']).dt.month
    df = df.drop('date',axis=1)
    return df

# level 5

def create_column_high_value_order(df:DataFrame,base_column,new_column):
    avg_total_amount = df[base_column].mean()
    df[new_column] = df.apply(lambda row: True if row.total_amount > avg_total_amount else False,axis=1)

def sort_data_frame(df:DataFrame, sort_column:str,asc=True) -> DataFrame:
    return df.sort_values(sort_column,ascending=asc)

