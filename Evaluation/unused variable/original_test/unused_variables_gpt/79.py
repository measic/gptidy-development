# define model
model = Sequential()
model.add(LSTM(n_neurons, batch_input_shape=(batch_size, window_size, 1), stateful=stateful, return_sequences=True))
model.add(LSTM(n_neurons, stateful=stateful, return_sequences=True))
model.add(TimeDistributed(Dense(n_classes, activation='softmax')))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.summary()