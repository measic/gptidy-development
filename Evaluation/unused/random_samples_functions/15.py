# invert differenced value
def inverse_difference(history, yhat, interval=1):
    return yhat+history[-interval]

# scale train and test data to [-1,1]
def scale(train,test):
    # fit scaler
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler=scaler.fit(train)
    # transform train
    train = train.reshape(train.shape[0],train.shape[1])
    train_scaled=scaler.transform(train)
    # transform test
    test = test.reshape(test.shape[0],test.shape[1])
    test_scaled=scaler.transform(test)
    return scaler, train_scaled, test_scaled

# inverse scaling for a forecasted value
def invert_scale(scaler,X,value):
    new_row=[x for x in X] +[value]
    array=numpy.array(new_row)
    array=array.reshape(1,len(array))
    inverted=scaler.inverse_transform(array)
    return inverted[0,-1]

# fit an LSTM network to training data
def fit_lstm(train, batch_size, nb_epoch, neurons):
    X,y=train[:,0:-1],train[:,-1]
    X=X.reshape(X.shape[0],1,X.shape[1])
    model=Sequential()
    model.add(LSTM(neurons,batch_input_shape=(batch_size,X.shape[1],X.shape[2]),stateful=True))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error",optimizer="adam")
    for i in range(nb_epoch):
        model.fit(X,y,epochs=1,batch_size=batch_size,verbose=0,shuffle=False)
        model.reset_states()
    return model

