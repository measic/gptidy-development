labels=pd.date_range(start="1901-1-1",periods=len(series),freq="MS")
# Man this frequency is tricky. If just say M, it means month end.....
labels
series.index=labels