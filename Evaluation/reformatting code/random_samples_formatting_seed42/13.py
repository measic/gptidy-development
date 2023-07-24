# Repeat the experiment
# Man this is taking a lot of time here 
repeats =30
error_scores=list()
for r in range(repeats):
    #firt the model
    lstm_model=fit_lstm(train_scaled,1,3000,4)
    #forecast the entire training dataset to build up state for forecasting
    train_reshaped=train_scaled[:,0].reshape(len(train_scaled),1,1)
    lstm_model.predict(train_reshaped,batch_size=1)
    # walk forward validation on the test data
    predictions=list()
    for i in range(len(test_scaled)):
        X,y=test_scaled[i,0:-1],test_scaled[i,-1]
        yhat = forecast_lstm(lstm_model,1,X)
        #invert scaling
        yhat=invert_scale(scaler,X,yhat)
        #invert differencing
        yhat=inverse_difference(raw_values,yhat,len(test_scaled)+1-i)
        #store forecast
        predictions.append(yhat)
    #report performance
    rmse=sqrt(mean_squared_error(raw_values[-12:],predictions))
    print("%d) Test RMSE: %.3f" % (r+1,rmse))
    error_scores.append(rmse)