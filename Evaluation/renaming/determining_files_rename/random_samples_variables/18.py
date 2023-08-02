def temporal_layer(x, n_neurons, dilation_rate, conv1d_kwargs, normalize=False, dropout=0):
    h = Conv1D(n_neurons, dilation_rate=dilation_rate, **conv1d_kwargs)(x)
    if normalize:
        h = BatchNormalization()(h)
    h = Activation('relu')(h)
    if dropout:
        h = Dropout(dropout)(h)
    return h

def temporal_block(h0, n_neurons, dilation_rate, conv1d_kwargs, normalize=False, dropout=0):
    h1 = temporal_layer(h0, n_neurons, dilation_rate, conv1d_kwargs, normalize=normalize, dropout=dropout)
    variable_def = temporal_layer(h1, n_neurons, dilation_rate, conv1d_kwargs, normalize=normalize, dropout=dropout)
    res = Conv1D(n_neurons, kernel_size=1)(h0) if h0.shape != variable_def.shape else h0
    block = Add()([res, variable_def])
    return Activation('relu')(block)
print(input_shape, 2 ** n_hidden)
loss = msig.classification_type + '_crossentropy'
fc_act = classifier_activation[msig.classification_type]
out_neurons = 1 if msig.classification_type == 'binary' else n_classes
conv1d_kwargs = dict(kernel_size=kernel_size, padding='causal')
compile_kwargs = dict(loss=loss, optimizer='adam', metrics=['accuracy'])
x = Input(shape=input_shape)
h = temporal_block(x, n_neurons, 1, conv1d_kwargs, normalize=False)
for d in range(1, n_hidden):
    h = temporal_block(h, n_neurons, 2 ** d, conv1d_kwargs, normalize=False)
z = Dense(out_neurons, activation=fc_act)(h)
model = Model(inputs=[x], outputs=[z])
model.compile(**compile_kwargs)
model.summary()