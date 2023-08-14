x = Input(batch_shape=(batch_size, window_size, 1))
z1 = PLSTM(n_neurons, return_sequences=True, implementation=2)(x)
z2 = PLSTM(n_neurons, return_sequences=True, implementation=2)(z1)
z = Dense(n_classes, activation='softmax')(z2)

model = Model(inputs=[x], outputs=[z])
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.summary()