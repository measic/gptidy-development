train3, test3 = df_per_day.iloc[:300,13], df_per_day.iloc[300:,13]


model3 = ExponentialSmoothing(train3, seasonal='mul', seasonal_periods=12).fit()
pred3 = model3.predict(start=test3.index[0], end=test3.index[-1])


(mean_absolute_error(np.exp(test3), np.exp(pred3)))