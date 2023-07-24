# Define loss and optimizer
weights = tf.multiply(targets, POS_WEIGHT) + 1
loss = tf.reduce_mean(tf.losses.sparse_softmax_cross_entropy(
    logits=pred,
    labels=targets,
    weights=weights), name='loss')
train_step = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss, name='train_step')

# Evaluate model
correct_pred = tf.equal(prediction, targets)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))