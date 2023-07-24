#Model suggestion

I['LSTM'] = Input(shape=(maxlen-1,), name="input")
E['LSTM'] = Embedding(len(tokens), embedding_size, mask_zero=True, name="embedding")(I['LSTM'])

#your network here
H['LSTM'] = LSTM(hidden_size, activation='relu', dropout=dropout, recurrent_dropout=recurrent_dropout, unroll=True, return_sequences=True)(E['LSTM'])
#H['LSTM'] = CuDNNLSTM(hidden_size)(E['LSTM'])

R['LSTM'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["LSTM"])

Y['LSTM'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['LSTM'])

models['LSTM'] = Model(inputs = [I['LSTM']], outputs = [Y['LSTM']])
models['LSTM'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['LSTM'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['LSTM'] = models['LSTM'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size).history

#save
with open("LSTMmodel_"+str(embedding_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['LSTM'], file)
models['LSTM'].save("LSTMmodel_"+str(embedding_size)+'_'+str(hidden_size))