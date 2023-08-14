df_per_day_train1, df_per_day_test1 = df_per_day.iloc[:300,1], df_per_day.iloc[300:,1]


model1 = ExponentialSmoothing(df_per_day_train1, seasonal='mul', seasonal_periods=12).fit()
pred1 = model1.predict(start=df_per_day_test1.index[0], end=df_per_day_test1.index[-1])


mean_absolute_error(df_per_day_test1, pred1)