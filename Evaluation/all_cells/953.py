
#What does the sequential thing do? Is it the same practice of 
#calling the model first?
'''
model=Sequential()
model.add(layer=LSTM(neurons, batch_input_shape=(batch_size, X.shape[1],X.shape[2]),stateful=True))
model.add(Dense(1)) #Is this defining the memory units 
model.compile(loss="mean_squared_error",optimizer='adam')

#What's adam? what's Dense? What's batch_input_shape?
'''
