predictions = list()
for i in range(len(test_scaled)):
    variable_def, y = (test_scaled[i, 0:-1], test_scaled[i, -1])
    yhat = forecast_lstm(lstm_model, 1, variable_def)
    yhat = invert_scale(scaler, variable_def, yhat)
    yhat = inverse_difference(raw_values, yhat, len(test_scaled) + 1 - i)
    predictions.append(yhat)
    expected = raw_values[len(train) + i + 1]
    print('Month=%d, Predicted=%f, Expected=%f' % (i + 1, yhat, expected))
rmse = sqrt(mean_squared_error(raw_values[-12:], predictions))
print('Test RMSE: %.3f' % rmse)
pyplot.plot(raw_values[-12:])
pyplot.plot(predictions)
pyplot.show()