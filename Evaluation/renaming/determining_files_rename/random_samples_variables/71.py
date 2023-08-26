n_epochs = 10
batch_size = 40
n_iterations_per_epoch = len(flower_paths_and_classes_train) // batch_size
with tf.Session() as sess:
    init.run()
    inception_saver.restore(sess, INCEPTION_V3_CHECKPOINT_PATH)
    for epoch in range(n_epochs):
        print('Epoch', epoch, end='')
        for iteration in range(n_iterations_per_epoch):
            print('.', end='')
            variable_def, y_batch = prepare_batch(flower_paths_and_classes_train, batch_size)
            sess.run(training_op, feed_dict={X: variable_def, y: y_batch, training: True})
        acc_train = accuracy.eval(feed_dict={X: variable_def, y: y_batch})
        print('  Train accuracy:', acc_train)
        save_path = saver.save(sess, './my_flowers_model')