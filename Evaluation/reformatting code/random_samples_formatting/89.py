# make a one-step forecast
def forecast_lstm(model, batch_size, X):
    X=X.reshape(1,1,len(X))
    yhat=model.predict(X,batch_size=batch_size)
    return yhat[0,0]

# load the dataset
series=read_csv(filename, header=0,parse_dates=[0],index_col=0,squeeze=True)

# transform data to be staionary
raw_values=series.values
diff_values=difference(raw_values,1)

# transform data to be supervised learning
supervised = timeseries_to_supervised(diff_values,1)
supervised_values=supervised.values

# split data into train and test-sets
train,test=supervised_values[0:-12],supervised_values[-12:]

# transform the scale of the data
scaler, train_scaled, test_scaled = scale(train, test)

