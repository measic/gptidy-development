x = Input(batch_shape=(batch_size, window_size, n_features))
z1 = LSTM(n_neurons, return_sequences=True, stateful=stateful)(x)
z2 = LSTM(n_neurons, return_sequences=False, stateful=stateful)(z1)
z = Dense(n_classes, activation='softmax')(z2)
# z = TimeDistributed(Dense(n_classes, activation='softmax'))(z2)

model = Model(inputs=[x], outputs=[z])
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.summary()