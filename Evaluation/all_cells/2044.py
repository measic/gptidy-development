model = sm.tsa.ARIMA(df_train_log,(0,0,2)).fit()
predictions_log = model.predict(40,42,dynamic=True)
predictions_log