with tf.variable_scope("decoder", dtype="float32") as scope:
    if use_bidirectional_encoder:
        decoder_cells = []
        for i in range(2):
            decoder_cell = tf.contrib.rnn.BasicLSTMCell(cell_size)
            decoder_cell = tf.contrib.rnn.DropoutWrapper(decoder_cell, input_keep_prob=0.8)
            decoder_cells.append(decoder_cell)
        decoder_cell = tf.contrib.rnn.MultiRNNCell(decoder_cells)

        if use_attention:
            if is_time_major:
                attention_states = tf.transpose(encoder_outputs, [1, 0, 2])
            else:
                attention_states = encoder_outputs
            attention_mechanism = tf.contrib.seq2seq.LuongAttention(
                cell_size, attention_states, memory_sequence_length=dataset.src_size,
                scale=True
            )
            decoder_cell = tf.contrib.seq2seq.AttentionWrapper(
                decoder_cell, attention_mechanism, attention_layer_size=cell_size,
                name="attention"
            )
            if is_time_major:
                decoder_initial_state = decoder_cell.zero_state(
                    tf.shape(decoder_emb_inp)[1], tf.float32).clone(cell_state=encoder_state)
            else:
                decoder_initial_state = decoder_cell.zero_state(
                    tf.shape(decoder_emb_inp)[0], tf.float32).clone(cell_state=encoder_state)
        else:
            decoder_initial_state = encoder_state
            
    else:
        decoder_cell = tf.contrib.rnn.BasicLSTMCell(cell_size)
        decoder_initial_state = encoder_state
        
    helper = tf.contrib.seq2seq.TrainingHelper(
        decoder_emb_inp, dataset.tgt_size, time_major=is_time_major)
    decoder = tf.contrib.seq2seq.BasicDecoder(
        decoder_cell, helper, decoder_initial_state)
    
    outputs, final, _ = tf.contrib.seq2seq.dynamic_decode(
        decoder, output_time_major=is_time_major, swap_memory=True, scope=scope)
    
    output_proj = layers_core.Dense(dataset.tgt_vocab_size, name="output_proj")
    logits = output_proj(outputs.rnn_output)
    
    