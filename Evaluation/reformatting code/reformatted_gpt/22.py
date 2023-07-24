train4, test4 = df_per_day.iloc[:295, 13], df_per_day.iloc[295:, 13]

model4 = ExponentialSmoothing(train4, seasonal='mul', seasonal_periods=12).fit()
pred4 = model4.predict(start=test4.index[0], end=test4.index[-1])

mean_absolute_error(np.exp(test4), np.exp(pred4))