hidden_size = 64
H2 = {}

I['GRU_64_64'] = Input(shape=(maxlen-1,), name="input")

#Using the embedding layer of the best performing network of previous exercice. (E["LSTM"])
E['GRU_64_64'] = Embedding(len(tokens), embedding_size, embeddings_initializer=Constant(lstm_embedding),
                            input_length=24,
                            trainable=False)(I['GRU_64_64'])

#your network here
H['GRU_64_64'] = GRU(hidden_size, activation='relu', dropout=dropout,
                     recurrent_dropout=recurrent_dropout, unroll=True,
                     return_sequences=True)(E['GRU_64_64'])
H2['GRU_64_64'] = GRU(hidden_size, activation='relu', dropout=dropout,
                      recurrent_dropout=recurrent_dropout, unroll=True,
                     return_sequences=True)(H['GRU_64_64'])


R['GRU_64_64'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["GRU_64_64"])

Y['GRU_64_64'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['GRU_64_64'])

models['GRU_64_64'] = Model(inputs = [I['GRU_64_64']], outputs = [Y['GRU_64_64']])
models['GRU_64_64'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['GRU_64_64'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['GRU_64_64'] = models['GRU_64_64'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size,
                                    callbacks = [callback]).history

#save
with open("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['GRU_64_64'], file)
models['GRU_64_64'].save("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size)+'_'+str(hidden_size))