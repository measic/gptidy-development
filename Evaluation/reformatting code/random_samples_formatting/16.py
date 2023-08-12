# fit the model
lstm_model=fit_lstm(train_scaled,1,3000,4)
# forecast the entire training dataset to build up state for forecasting
train_reshaped=train_scaled[:,0].reshape(len(train_scaled),1,1)
lstm_model.predict(train_reshaped,batch_size=1)
