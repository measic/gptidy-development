# Bidirectional RNN
bi_outputs, _ = tf.nn.bidirectional_dynamic_rnn(
    cell_fw = cell_fw,
    cell_bw = cell_bw,
    inputs = inpts,
    sequence_length = length,
    dtype = tf.float32)

outputs = tf.concat(bi_outputs, -1, name='outputs')

# pred = tf.matmul(outputs, W)
# pred = tf.scan(lambda a, x: tf.matmul(x, W), outputs, infer_shape=False)
pred = tf.layers.dense(inputs=outputs,
                       units=n_classes,
                       name='pred')
prediction = tf.argmax(pred, axis=-1, name='prediction')