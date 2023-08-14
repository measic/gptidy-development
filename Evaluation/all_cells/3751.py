with tf.variable_scope("greedy_decoder"):
    g_helper = tf.contrib.seq2seq.GreedyEmbeddingHelper(
        embedding, tf.fill([dataset.config.batch_size], dataset.SOS), dataset.EOS)
    g_decoder = tf.contrib.seq2seq.BasicDecoder(decoder_cell, g_helper, decoder_initial_state,
                                             output_layer=output_proj)

    g_outputs, _, _ = tf.contrib.seq2seq.dynamic_decode(g_decoder, maximum_iterations=30)