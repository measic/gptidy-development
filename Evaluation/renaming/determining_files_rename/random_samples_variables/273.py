with tf.variable_scope('train'):
    if is_time_major:
        variable_def = tf.transpose(variable_def, [1, 0, 2])
        crossent = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=dataset.tgt_out_ids, logits=variable_def)
        target_weights = tf.sequence_mask(dataset.tgt_size, tf.shape(variable_def)[1], tf.float32)
    else:
        crossent = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=dataset.tgt_out_ids, logits=variable_def)
        target_weights = tf.sequence_mask(dataset.tgt_size, tf.shape(variable_def)[1], tf.float32)
    loss = tf.reduce_sum(crossent * target_weights) / tf.to_float(batch_size)
    tf.summary.scalar('loss', loss)
    learning_rate = tf.placeholder(dtype=tf.float32, name='learning_rate')
    max_global_norm = tf.placeholder(dtype=tf.float32, name='max_global_norm')
    optimizer = tf.train.MomentumOptimizer(learning_rate, momentum=0.5)
    params = tf.trainable_variables()
    gradients = tf.gradients(loss, params)
    for grad, var in zip(gradients, params):
        tf.summary.histogram(var.op.name + '/gradient', grad)
    gradients, _ = tf.clip_by_global_norm(gradients, max_global_norm)
    for grad, var in zip(gradients, params):
        tf.summary.histogram(var.op.name + '/clipped_gradient', grad)
    update = optimizer.apply_gradients(zip(gradients, params))