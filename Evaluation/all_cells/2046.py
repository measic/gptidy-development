#LOG
train1, test1 = log_and_placements_aggregated_per_week_df.iloc[:39,18], log_and_placements_aggregated_per_week_df.iloc[39:,18]


model1 = ExponentialSmoothing(train1, seasonal='mul', seasonal_periods=12).fit()
pred1 = model1.predict(start=test1.index[0], end=test1.index[-1])


mean_absolute_error(np.exp(test1),np.exp(pred1))