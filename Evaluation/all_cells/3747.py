with tf.variable_scope("embedding"):
    embedding = tf.get_variable("embedding", [dataset.src_vocab_size, embedding_dim], dtype=tf.float32)
    embedding_input = tf.nn.embedding_lookup(embedding, dataset.src_ids)
    decoder_emb_inp = tf.nn.embedding_lookup(embedding, dataset.tgt_in_ids)
    if is_time_major:
        embedding_input = tf.transpose(embedding_input, [1, 0, 2])
        decoder_emb_inp = tf.transpose(decoder_emb_inp, [1, 0, 2])