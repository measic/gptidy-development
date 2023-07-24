# Helper function that takes numpy array of the raw time series and a lag or number of shifted series to create 
# and use as inputs
def timeseries_to_supervised(data,lag=1):
    df=pd.DataFrame(data)
    columns=[df.shift(i) for i in range(1,lag+1)] # depends on how many lags are required
    columns.append(df) # Appending list to each other 
    df=pd.concat(columns,axis=1)
    df.fillna(0,inplace=True) #takes care of the Nan value
    return df