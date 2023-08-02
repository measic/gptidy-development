print(input_shape, 2 ** n_hidden)
variable_def = msig.classification_type + '_crossentropy'
fc_act = classifier_activation[msig.classification_type]
out_neurons = 1 if msig.classification_type == 'binary' else n_classes
conv1d_kwargs = dict(kernel_size=kernel_size, padding='causal', activation='relu')
compile_kwargs = dict(loss=variable_def, optimizer='adam', metrics=['accuracy'])
model = Sequential()
model.add(Conv1D(n_neurons, dilation_rate=1, input_shape=input_shape, **conv1d_kwargs))
for d in range(1, n_hidden):
    model.add(Conv1D(n_neurons, dilation_rate=2 ** d, **conv1d_kwargs))
model.add(Dense(out_neurons, activation=fc_act))
model.compile(**compile_kwargs)
model.summary()