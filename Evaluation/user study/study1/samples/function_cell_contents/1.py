from dateutil.parser import parse
from datetime import datetime
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
df = pd.read_csv('hotels_data.csv')


def function_def(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y %H:%M')


df['DayDiff'] = DataFrame([function_def(val) for val in df['Checkin Date']]) - \
    DataFrame([function_def(val) for val in df['Snapshot Date']])
df['WeekDay'] = DataFrame([function_def(val).weekday()
                          for val in df['Checkin Date']])
df['DiscountDiff'] = df['Original Price'] - df['Discount Price']
df['DiscountPerc'] = df['DiscountDiff'] / df['Original Price'] * 100
df
