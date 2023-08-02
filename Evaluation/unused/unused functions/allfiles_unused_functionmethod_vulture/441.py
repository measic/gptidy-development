def evaluate(X_data, y_data, b, lr):
    num_examples = len(X_data)
    total_accuracy = 0
    sess = tf.get_default_session()
    for offset in range(0, num_examples, BATCH_SIZE):
        batch_x, batch_y = X_data[offset:offset+BATCH_SIZE], y_data[offset:offset+BATCH_SIZE]
        summary, accuracy = sess.run([summary_op,accuracy_operation], feed_dict={tf_train_dataset : batch_x, tf_train_labels : batch_y, 
                         tf_beta: b, tf_keep_prob : 1, tf_learning_rate : lr})
        total_accuracy += (accuracy * len(batch_x))
    return summary, total_accuracy / num_examples
