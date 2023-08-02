n_epochs = 10
batch_size = 40
variable_def = len(flower_paths_and_classes_train) // batch_size
with tf.Session() as sess:
    init.run()
    inception_saver.restore(sess, INCEPTION_V3_CHECKPOINT_PATH)
    for epoch in range(n_epochs):
        print('Epoch', epoch, end='')
        for iteration in range(variable_def):
            print('.', end='')
            X_batch, y_batch = prepare_batch(flower_paths_and_classes_train, batch_size)
            sess.run(training_op, feed_dict={X: X_batch, y: y_batch, training: True})
        acc_train = accuracy.eval(feed_dict={X: X_batch, y: y_batch})
        print('  Train accuracy:', acc_train)
        save_path = saver.save(sess, './my_flowers_model')