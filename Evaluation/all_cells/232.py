num_steps = 40001

with tf.Session(graph=graph) as session:
    tf.initialize_all_variables().run()
    start = datetime.datetime.now()
    print('Initialized')
    for step in range(num_steps):
        offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
        batch_data = train_dataset[offset:(offset + batch_size), :, :, :]
        batch_labels = train_labels[offset:(offset + batch_size), :]
        feed_dict = {tf_train_dataset : batch_data, tf_train_labels : batch_labels,
                    keep3:0.9, keep4:0.9}
        _, l, predictions = session.run(
            [optimizer, loss, train_prediction], feed_dict=feed_dict)
        if (step % 500 == 0):
            ends = eta(start, step, num_steps)
            valpred = valid_prediction.eval(feed_dict={keep3:1.0, keep4:1.0})            
            print('Step %d - Loss %f - Minibatch %.1f%% - Validation %.1f%% - ETA %s' %
                  (step, l, accuracy(predictions, batch_labels), accuracy(valpred, valid_labels), ends))
    print('Test accuracy: %.1f%%' %
          accuracy(test_prediction.eval(feed_dict={keep3:1.0, keep4:1.0}), test_labels))