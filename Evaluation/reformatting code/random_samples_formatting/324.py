save_file= './train_model_best.ckpt'
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session, save_file)
    
    _, test_accuracy = evaluate(X_test, y_test, b = BETA, lr = LEARNING_RATE)
    print("Test Accuracy = {:.3f}".format(test_accuracy))