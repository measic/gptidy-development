train2, test2 = log_and_placements_aggregated_per_week_df.iloc[:31,1], log_and_placements_aggregated_per_week_df.iloc[31:,1]


model2 = ExponentialSmoothing(train2, seasonal='mul', seasonal_periods=12).fit()
pred2 = model2.predict(start=test2.index[0], end=test2.index[-1])


mean_absolute_error(test2, pred2)