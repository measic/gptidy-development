#Model suggestion

I['RNN'] = Input(shape=(maxlen-1,), name="input")
E['RNN'] = Embedding(len(tokens), embedding_size, mask_zero=True, input_length=24, name="embedding")(I['RNN'])

#your network here
H['RNN'] = SimpleRNN(hidden_size,activation='relu', dropout=dropout, recurrent_dropout=recurrent_dropout, unroll=True, return_sequences=True)(E['RNN'])

R['RNN'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["RNN"])

Y['RNN'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['RNN'])


models['RNN'] = Model(inputs = [I['RNN']], outputs = [Y['RNN']])
models['RNN'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['RNN'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['RNN'] = models['RNN'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size).history

#save
with open("RNNmodel_"+str(embedding_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['RNN'], file)
models['RNN'].save("RNNmodel_"+str(embedding_size)+'_'+str(hidden_size))