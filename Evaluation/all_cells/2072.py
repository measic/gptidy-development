plt.plot(df_per_day_train.index, df_per_day_train, label='Train')
plt.plot(df_per_day_test.index, df_per_day_test, label='Test')
plt.plot(predictions.index, predictions, label='ARIMA(1,0,4) LOG')
plt.legend(loc='best')