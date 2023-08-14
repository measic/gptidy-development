hidden_size = 256

I['GRU_256'] = Input(shape=(maxlen-1,), name="input")

#Using the embedding layer of the best performing network of previous exercice. (E["LSTM"])
E['GRU_256'] = Embedding(len(tokens), embedding_size, embeddings_initializer=Constant(lstm_embedding),
                            input_length=24,
                            trainable=False)(I['GRU_256'])

#your network here
H['GRU_256'] = GRU(hidden_size, activation='relu', dropout=dropout, recurrent_dropout=recurrent_dropout, unroll=True, return_sequences=True)(E['GRU_256'])
#H['GRU'] = CuDNNGRU(hidden_size)(E['GRU'])

R['GRU_256'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["GRU_256"])

Y['GRU_256'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['GRU_256'])

models['GRU_256'] = Model(inputs = [I['GRU_256']], outputs = [Y['GRU_256']])
models['GRU_256'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['GRU_256'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['GRU_256'] = models['GRU_256'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size,
                                    callbacks = [callback]).history

#save
with open("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['GRU_256'], file)
models['GRU_256'].save("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size))