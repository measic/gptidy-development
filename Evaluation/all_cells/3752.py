if use_attention is False:
    with tf.variable_scope("beam_search"):
        beam_width = 4
        start_tokens = tf.fill([config.batch_size], dataset.SOS)
        bm_dec_initial_state = tf.contrib.seq2seq.tile_batch(
            encoder_state, multiplier=beam_width)
        bm_decoder = tf.contrib.seq2seq.BeamSearchDecoder(
            cell=decoder_cell,
            embedding=embedding,
            start_tokens=start_tokens,
            initial_state=bm_dec_initial_state,
            beam_width=beam_width,
            output_layer=output_proj,
            end_token=dataset.EOS
        )
        bm_outputs, _, _ = tf.contrib.seq2seq.dynamic_decode(
            bm_decoder, maximum_iterations=config.tgt_maxlen)