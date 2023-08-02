n_epochs = 10
variable_def = 100
with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        for iteration in range(mnist.train.num_examples // variable_def):
            X_batch, y_batch = mnist.train.next_batch(variable_def)
            sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
        acc_train = accuracy.eval(feed_dict={X: X_batch, y: y_batch})
        acc_test = accuracy.eval(feed_dict={X: mnist.test.images, y: mnist.test.labels})
        print(epoch, 'Train accuracy:', acc_train, 'Test accuracy:', acc_test)
        save_path = saver.save(sess, './my_mnist_model')