# walk forward validation on the test data
predictions=list()
for i in range(len(test_scaled)):
    # make one step forecast
    X,y=test_scaled[i,0:-1],test_scaled[i,-1]
    yhat=forecast_lstm(lstm_model,1,X)
    # invert scaling
    yhat=invert_scale(scaler,X,yhat)
    # invert differencing
    yhat=inverse_difference(raw_values,yhat,len(test_scaled)+1-i)
    # store forecast
    predictions.append(yhat)
    expected=raw_values[len(train)+i+1]
    print('Month=%d, Predicted=%f, Expected=%f' % (i+1, yhat, expected))
    
# report performance
rmse=sqrt(mean_squared_error(raw_values[-12:],predictions))
print("Test RMSE: %.3f" %rmse)

# line pot of observed vs predicted 
pyplot.plot(raw_values[-12:])
pyplot.plot(predictions)
pyplot.show()