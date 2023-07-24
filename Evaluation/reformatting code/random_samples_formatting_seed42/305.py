context = Input(shape=(maxlen,), name="input_context")
shared_embedding =  Embedding(len(tokens), embedding_size, embeddings_initializer=Constant(lstm_embedding),
                            trainable=False)

context_embedding = shared_embedding(context)

encoder_y, encoder_h, encoder_c = CuDNNLSTM(128, 
            return_sequences=False,
            return_state=True,
            stateful=False,
            go_backwards=True,
            name="encoder")(context_embedding)

answer = Input(shape=(maxlen-1,), name="input_answer")
answer_embedding = shared_embedding(answer)

decoder = CuDNNLSTM(128, 
            return_sequences=True,
            stateful=False,
            name="decoder")(answer_embedding, initial_state=[encoder_h, encoder_c])

drop = Dropout(0.5)(decoder)
decoder2 = CuDNNLSTM(128, 
            return_sequences=True,
            stateful=False,
            name="decoder2")(drop)

R = TimeDistributed(Dense(embedding_size, activation='relu'), name='readout')(decoder2)
Y = TimeDistributed(Dense(len(tokens), activation='softmax'), name='output')(R)

Chatbot = Model(inputs = [context, answer], outputs = [Y])
Chatbot.compile(
    loss='categorical_crossentropy', 
    optimizer=Adam(),
    metrics=['acc'])
Chatbot.summary()