df_per_day_train2, df_per_day_test2 = df_per_day.iloc[:295,1], df_per_day.iloc[295:,1]


model2 = ExponentialSmoothing(df_per_day_train2, seasonal='mul', seasonal_periods=12).fit()
pred2 = model2.predict(start=df_per_day_test2.index[0], end=df_per_day_test2.index[-1])


mean_absolute_error(df_per_day_test2, pred2)