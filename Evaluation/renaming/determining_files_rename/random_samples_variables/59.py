predictions = list()
for i in range(len(test_scaled)):
    X, y = (test_scaled[i, 0:-1], test_scaled[i, -1])
    yhat = forecast_lstm(lstm_model, 1, X)
    yhat = invert_scale(scaler, X, yhat)
    yhat = inverse_difference(raw_values, yhat, len(test_scaled) + 1 - i)
    predictions.append(yhat)
    variable_def = raw_values[len(train) + i + 1]
    print('Month=%d, Predicted=%f, Expected=%f' % (i + 1, yhat, variable_def))
rmse = sqrt(mean_squared_error(raw_values[-12:], predictions))
print('Test RMSE: %.3f' % rmse)
pyplot.plot(raw_values[-12:])
pyplot.plot(predictions)
pyplot.show()