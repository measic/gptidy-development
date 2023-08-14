#Model suggestion

I['GRU'] = Input(shape=(maxlen-1,), name="input")
E['GRU'] = Embedding(len(tokens), embedding_size, mask_zero=True, name="embedding")(I['GRU'])

#your network here
H['GRU'] = GRU(hidden_size, activation='relu', dropout=dropout, recurrent_dropout=recurrent_dropout, unroll=True, return_sequences=True)(E['GRU'])
#H['GRU'] = CuDNNGRU(hidden_size)(E['GRU'])

R['GRU'] = TimeDistributed(Dense(embedding_size, activation="relu"), name='readout')(H["GRU"])

Y['GRU'] = TimeDistributed(Dense(len(tokens), activation="softmax"), name='output')(R['GRU'])


models['GRU'] = Model(inputs = [I['GRU']], outputs = [Y['GRU']])
models['GRU'].compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
models['GRU'].summary()

print(X[:,:-1].shape, T[:,1:].shape)
logs['GRU'] = models['GRU'].fit({'input': X[:dataset_cut,:-1]}, {'output': T[:dataset_cut,1:]}, 
                                    epochs=epochs, 
                                    validation_split=validation_split, 
                                    batch_size=batch_size).history

#save
with open("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size)+"_log.pkl", "wb") as file:
    pickle.dump(logs['GRU'], file)
models['GRU'].save("GRUmodel_"+str(embedding_size)+'_'+str(hidden_size))