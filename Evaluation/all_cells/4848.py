#Model suggestion
hidden_size = 128

I['GRU_128'] = Input(shape=(maxlen-1,), name="input")

E['GRU_128'] = Embedding(len(tokens), embedding_size, embeddings_initializer=Constant(lstm_embedding),
                            trainable=False)(I['GRU_128'])

#your network here
H['GRU_128'] = GRU(hidden_size, activation='relu', dropout=dropout, recurrent_dropout=recurrent_dropout, unroll=True, return_sequences=True)(E['GRU_128'])
#H['GRU'] = CuDNNGRU(hidden_size)(E['GRU'])

R['GRU_128'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["GRU_128"])

Y['GRU_128'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['GRU_128'])

models['GRU_128'] = Model(inputs = [I['GRU_128']], outputs = [Y['GRU_128']])
models['GRU_128'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['GRU_128'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['GRU_128'] = models['GRU_128'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size,
                                    callbacks = [callback]).history

#save
with open("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['GRU_128'], file)
models['GRU_128'].save("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size))