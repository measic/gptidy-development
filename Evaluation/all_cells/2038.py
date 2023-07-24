model = sm.tsa.ARIMA(df_train,(1,0,0)).fit()

predictions = model.predict(40,42,dynamic=True)

predictions