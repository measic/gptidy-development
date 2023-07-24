def train_model(beta, lr, name_ext, learn_decay):
    best_model_validation_acc = 0
    valid_acc_list = []
    train_acc_list = []
    
    save_file = './train_model_' + 'best' + '.ckpt'
    num_examples = X_train.shape[0]
    step = 0
    
    saver = tf.train.Saver()
    
    with tf.Session() as session:
        
        if(RELOAD_MODEL):
            # Load the weights and bias
            saver.restore(session, save_file)
        else:         
            session.run(tf.global_variables_initializer())
            
        print('tensorboard loc:', 'log-directory/' + str.replace(name_ext,'_','/') + '/train')
        train_writer = tf.summary.FileWriter('log-directory/' + str.replace(name_ext,'_','/') + '/train',session.graph)
        valid_writer =  tf.summary.FileWriter('log-directory/' + str.replace(name_ext,'_','/') + '/valid')

        for epoch in range(EPOCHS):

            if(learn_decay and epoch > 0 and epoch % 30 == 0 and lr > 1e-6):
                lr = lr/2
            
            # shuffling
            X_train_subset, y_train_subset = shuffle(X_train, y_train)

            # Train for all the mini-batches in the epoch
            for offset in range(0, num_examples, BATCH_SIZE):
                step += 1
                
                end = offset + BATCH_SIZE
                batch_x, batch_y = X_train_subset[offset:end], y_train_subset[offset:end]

                feed_dict = {tf_train_dataset : batch_x, tf_train_labels : batch_y, 
                             tf_beta: BETA, tf_keep_prob : 0.5, tf_learning_rate : lr}

                session.run([optimizer], feed_dict = feed_dict)

            # at the end of the epoch, gather statistics
            training_summary, training_accuracy = evaluate(X_train, y_train, b = beta, lr = lr)
            train_writer.add_summary(training_summary, step)
            valid_summary, validation_accuracy = evaluate(X_valid, y_valid, b = beta, lr = lr)
            valid_writer.add_summary(valid_summary, step)
            print('Step %s / Epoch %s: Training accuracy: %s, Validation accuracy: %s' % (step, epoch, training_accuracy, validation_accuracy))
            valid_acc_list.append(validation_accuracy)
            train_acc_list.append(training_accuracy)

            if(epoch == 9 and validation_accuracy<0.9):
                print('break')
                break

            if(validation_accuracy > best_model_validation_acc):
                best_model_validation_acc = validation_accuracy
                
                saver.save(session, save_file) 
                print("Model saved at: ", save_file) 

        test_summary, test_accuracy = evaluate(X_test, y_test, b = beta, lr = lr)  
        print('Step %s / Epoch %s: Test accuracy: %s' % (step, epoch,test_accuracy))
        train_writer.close()   
        valid_writer.close()   
        
    return train_acc_list, valid_acc_list