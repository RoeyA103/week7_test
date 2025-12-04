import pandas as pd
import numpy as np

def data_frame_conversion(df):
    def clean_sign(column):
        clean_column = column.apply(lambda x : x[:-2])
        return clean_column

    def reshape_to_float(column):
        reshaped = pd.to_numeric(column)
        return reshaped

    def reshape_to_datetime(column):
        reshaped = pd.to_datetime(column)
        return reshaped

    df.total_amount = clean_sign(df.total_amount)
    df.total_amount = reshape_to_float(df.total_amount)
    df.order_date = reshape_to_datetime(df.order_date)

    return df


import re

def cleanhtml_column(column):
    def cleanhtml(raw_html):
        CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub(CLEANR, ' ', raw_html)
        return cleantext
    
    clean = column.apply(cleanhtml)

    return clean

def fill_empty_col(column,text):
    full = column.apply(lambda x : text if x == "" else x)
    return full



def create_ordermonth_col(df):
    df['order_month'] = df.order_date.dt.month
    return df

def create_high_value_order(df):
    mean_amount = df.total_amount.mean()
    df["high_value_order"] = [True if x > mean_amount else False for x in df['total_amount']]  
    return df

def sort_by_total_amount(df):
    df = df.sort_values(by="total_amount",ascending=False)
    return df


def create_mean_rating_col(df):
    m_rating = df.groupby('country')['rating'].mean()
    mean_r_dict = m_rating.to_dict()

    df["mean_rating"] = [mean_r_dict[str(x)] for x in df.country]

    return df

def filter_by_amount_rating(df):
    df = df.loc[(df['rating'] > 4.5) & (df['total_amount'] > 1000)]
    return df


def create_delivery_status_col(df):
    df['delivery_status'] = ["delayed" if x > 7 else  "on time"  for x in df.shipping_days]
    return df
