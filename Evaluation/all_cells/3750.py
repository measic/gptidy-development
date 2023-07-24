with tf.variable_scope("encoder"):
    
    if use_bidirectional_encoder:
        fw_cell = tf.nn.rnn_cell.BasicLSTMCell(cell_size)
        fw_cell = tf.contrib.rnn.DropoutWrapper(fw_cell, input_keep_prob=0.8)
        bw_cell = tf.nn.rnn_cell.BasicLSTMCell(cell_size)
        bw_cell = tf.contrib.rnn.DropoutWrapper(bw_cell, input_keep_prob=0.8)

        o, e = tf.nn.bidirectional_dynamic_rnn(
            fw_cell, bw_cell, embedding_input, dtype='float32', sequence_length=dataset.src_size,
            time_major=is_time_major)
        encoder_outputs = tf.concat(o, -1)
        encoder_state = e
    
    else:
        fw_cell = tf.nn.rnn_cell.BasicLSTMCell(cell_size)
        fw_cell = tf.contrib.rnn.DropoutWrapper(fw_cell, input_keep_prob=0.8)
        o, e = tf.nn.dynamic_rnn(fw_cell, embedding_input, dtype='float32',
                                 sequence_length=dataset.src_size, time_major=is_time_major)
        encoder_outputs = o
        encoder_state = e
    