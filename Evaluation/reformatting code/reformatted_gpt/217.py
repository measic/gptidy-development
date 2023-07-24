#ignore
class MultiHeadAttentionDemo(tf.keras.layers.Layer):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttentionDemo, self).__init__()
        self.num_heads = num_heads
        self.d_model = d_model

        assert d_model % self.num_heads == 0

        self.depth = d_model // self.num_heads

        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)

        self.dense = tf.keras.layers.Dense(d_model)

    def split_heads(self, x, batch_size, draw=False, only_draw_reshape=False):
        """Split the last dimension into (num_heads, depth).
        Transpose the result such that the shape is (batch_size, num_heads, seq_len, depth)
        """
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        if draw:
            plot(x, name='tf.reshape in split_heads', shape_desc='\n(batch_size, seq_len, num_heads, depth)',
                 single_plot_size=8, h_dist_ratio=0.3, w_dist_ratio=0.3, width_prec=1.0 / 2 / 2, bottom_prec=1.0 / 8 * 2)

        x = tf.transpose(x, perm=[0, 2, 1, 3])
        if draw and not only_draw_reshape:
            plot(x, name='tf.transpose in split_heads', shape_desc='\n(batch-size, num_heads, seq_len, depth)')
        return x

    def call(self, v, k, q, mask, draw=False, only_draw_reshape=False):
        batch_size = tf.shape(q)[0]
        shape_desc = '\n(batch_size, seq_len, d_model)'

        if draw and not only_draw_reshape:
            plot(q, name="q", shape_desc=shape_desc)
            plot(k, name="k", shape_desc=shape_desc)
            plot(v, name="v", shape_desc=shape_desc)

        q = self.wq(q)  # (batch_size, seq_len, d_model)
        k = self.wk(k)  # (batch_size, seq_len, d_model)
        v = self.wv(v)  # (batch_size, seq_len, d_model)
        if draw and not only_draw_reshape:
            plot(q, name="q", shape_desc=shape_desc)
            plot(k, name="k", shape_desc=shape_desc)
            plot(v, name="v", shape_desc=shape_desc)

        q = self.split_heads(q, batch_size, draw)  # (batch_size, num_heads, seq_len_q, depth)
        k = self.split_heads(k, batch_size, draw)  # (batch_size, num_heads, seq_len_k, depth)
        v = self.split_heads(v, batch_size, draw)  # (batch_size, num_heads, seq_len_v, depth)

        # scaled_attention.shape == (batch_size, num_heads, seq_len_v, depth)
        # attention_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_k)
        if only_draw_reshape:
            scaled_attention, attention_weights = scaled_dot_product_attention(
                q, k, v, mask)
        else:
            scaled_attention, attention_weights = scaled_dot_product_attention_demo(
                q, k, v, mask)

        if draw and not only_draw_reshape:
            plot(scaled_attention, name='scaled_attention', shape_desc='\n(batch_size, num_heads, seq_len, depth)')
            plot(attention_weights, name='attention_weights', shape_desc='\n(batch_size, num_heads, seq_len_q, seq_len_k)')

        scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])  # (batch_size, seq_len_q, num_heads, depth)
        if draw:
            plot(scaled_attention, name='scaled_attention after transpose',
                 shape_desc='\n(batch_size, seq_len_q, num_heads, depth)',
                 single_plot_size=8, h_dist_ratio=0.3, w_dist_ratio=0.3, width_prec=1.0 / 2 / 2, bottom_prec=1.0 / 8 * 2)

        concat_attention = tf.reshape(scaled_attention,
                                      (batch_size, -1, self.d_model))  # (batch_size, seq_len_q, d_model)
        if draw and not only_draw_reshape:
            plot(concat_attention, name='concat_attention', shape_desc='\n(batch_size, seq_len_q, d_model)')

        output = self.dense(concat_attention)  # (batch_size, seq_len_q, d_model)
        if draw and not only_draw_reshape:
            plot(output, name='output', shape_desc='\n(batch-size, seq_len_q, d_model)')

        return output, attention_weights