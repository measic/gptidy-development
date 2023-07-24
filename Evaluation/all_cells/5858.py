for learning_rate in [3E-3]:
        print('Training with learning rate={}'.format(learning_rate))
        lenet_model = LeNetModel(logits, X_train, y_train, X_valid, y_valid, learning_rate, x, y , hold_prob, hparam='lr_{}'.format(learning_rate) )
        lenet_model.train(EPOCHS, BATCH_SIZE)