model = sm.tsa.ARIMA(df_per_day_train,(1,0,4)).fit()

predictions = model.predict(300,302,dynamic=True)

predictions