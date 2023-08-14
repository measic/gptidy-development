#ignore
# def split_heads_demo(x, d_model, num_heads):
#   # x.shape: (batch_size, seq_len, d_model)
#   batch_size = tf.shape(x)[0]
  
#   assert d_model % num_heads == 0
#   depth = d_model // num_heads  # 這是分成多頭以後每個向量的維度 
  
#   plot(x, name='x', shape_desc='\n(batch_size, seq_len, d_model)')
  
#   reshaped_x = tf.reshape(x, shape=(batch_size, -1, num_heads, depth))
#   plot(reshaped_x, name='reshaped_x', shape_desc='\n(batch_size, seq_len, num_heads, depth)',
#            single_plot_size=8, h_dist_ratio=0.3, w_dist_ratio=0.3, 
#        width_prec=1.0 / 2 / 2, bottom_prec=1.0 / 8 * 2, linewidths=2)
  
#   transposed_x = tf.transpose(reshaped_x, perm=[0, 2, 1, 3])
#   plot(transposed_x, name='output', shape_desc='\n(batch_size, num_heads, seq_len, depth)')
  
#   return transposed_x

# d_model = 4
# num_heads = 2

# two_heads_emb_inp = split_heads_demo(emb_inp, d_model, num_heads)  
