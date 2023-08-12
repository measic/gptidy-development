num_steps = 1001

with tf.Session(graph=graph) as session:
    tf.initialize_all_variables().run()
    print('Initialized')
    for step in range(num_steps):
        offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
        batch_data = train_dataset[offset:(offset + batch_size), :, :, :]
        batch_labels = train_labels[offset:(offset + batch_size), :]
        feed_dict = {tf_train_dataset : batch_data, tf_train_labels : batch_labels}
        _, l, predictions = session.run(
            [optimizer, loss, train_prediction], feed_dict=feed_dict)
        if (step % 50 == 0):
            print('Step %d - Loss %f - Minibatch %.1f%% - Validation %.1f%%' %
                  (step, l, accuracy(predictions, batch_labels),accuracy(
                    valid_prediction.eval(), valid_labels)))
    print('Test accuracy: %.1f%%' % accuracy(test_prediction.eval(), test_labels))