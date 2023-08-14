import numpy as np
import pandas as pd
from pandas import Series,DataFrame
df = pd.read_csv("hotels_data.csv")

from datetime import datetime
from dateutil.parser import parse

#parsing string to date time format
def get_datetime(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y %H:%M')

df["DayDiff"] = DataFrame([get_datetime(val) for val in df["Checkin Date"]]) - DataFrame([get_datetime(val) for val in df["Snapshot Date"]])
df["WeekDay"] = DataFrame([get_datetime(val).weekday() for val in df["Checkin Date"]])
df["DiscountDiff"] = df["Original Price"] - df["Discount Price"]
df["DiscountPerc"] = (df["DiscountDiff"]/df["Original Price"]) * 100

df