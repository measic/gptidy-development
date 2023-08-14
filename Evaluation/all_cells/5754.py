save_file= './train_model_best.ckpt'
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session, save_file)

    num_examples = len(X_test)

    ct = None
    labels_predicted = None
    for offset in range(0, num_examples, BATCH_SIZE):
        batch_x, batch_y = X_test[offset:offset+BATCH_SIZE], y_test[offset:offset+BATCH_SIZE]
        c,labels_predicted_temp = session.run([correct_prediction,labels_pred_cls], feed_dict={tf_train_dataset : batch_x, tf_train_labels : batch_y, 
                         tf_beta: BETA, tf_keep_prob : 1, tf_learning_rate : LEARNING_RATE})

        if ct is None:
            ct = c
            labels_predicted = labels_predicted_temp
        else:
            ct = np.concatenate((ct,c),axis = 0)
            labels_predicted = np.concatenate((labels_predicted,labels_predicted_temp),axis = 0)

    pred_error = (ct == False)
    X_error_original = X_test_original[pred_error]
    X_error = X_test[pred_error]
    y_error_true = y_test_cls[pred_error]
    y_error_pred = labels_predicted[pred_error]
