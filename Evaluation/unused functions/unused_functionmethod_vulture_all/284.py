#ignore
def scaled_dot_product_attention_demo(q, k, v, mask, draw=False):
  """Calculate the attention weights.
  q, k, v must have matching leading dimensions.
  k, v must have matching penultimate dimension, i.e.: seq_len_k = seq_len_v.
  The mask has different shapes depending on its type(padding or look ahead) 
  but it must be broadcastable for addition.
  
  Args:
    q: query shape == (..., seq_len_q, depth)
    k: key shape == (..., seq_len_k, depth)
    v: value shape == (..., seq_len_v, depth_v)
    mask: Float tensor with shape broadcastable 
          to (..., seq_len_q, seq_len_k). Defaults to None.
    
  Returns:
    output, attention_weights
  """
  labels= ['subwords in q', 'subwords in k']
  shape_desc = '\n(batch_size, seq_len_q, seq_len_k)'

  matmul_qk = tf.matmul(q, k, transpose_b=True)  # (..., seq_len_q, seq_len_k)
  if draw:
    plot(matmul_qk, name='matmul_qk', labels=labels, shape_desc=shape_desc)
  # scale matmul_qk
  dk = tf.cast(tf.shape(k)[-1], tf.float32)
  scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
  if draw:
    plot(scaled_attention_logits, name="scaled_attention_logits", 
         labels=labels, shape_desc=shape_desc)

  # add the mask to the scaled tensor.
  mask_name = ''
  if mask is not None:
    mask_name = 'masked_'
    orig_mask = mask
    # demo usage for q, k, v less than ndim=4
    if q.ndim == 4:
      pass
    elif q.ndim == 3 and mask.ndim == 4:
      orig_mask = mask
      mask = tf.squeeze(mask, axis=[1])
#       mask = tf.reshape(mask, shape=(mask.shape[0], 1, mask.shape[-1]))
    
    if draw:
      plot(mask, name="mask", 
         labels=['sentence', 'subwords in seq_q'], shape_desc='\n(batch_size, 1, seq_len_q)')
      
      temp_mask = mask * -1e9
      plot(temp_mask, name="mask", 
         labels=['sentence', 'subwords in seq_q'], shape_desc='\n(batch_size, 1, seq_len_q)')
      # padding mask broadcasting demo
#       for i in range(2, 9):
#         t = tf.constant(np.repeat(temp_mask, i, axis=1))

#         plot(t, name="mask", 
#          labels=['subwords in seq_q', 'subwords in seq_q'], shape_desc=f'\n(batch_size, {i}, seq_len_q)')
      
  
    scaled_attention_logits += (mask * -1e9)
    if draw:
      plot(scaled_attention_logits, name="scaled_attention_logits", 
           labels=labels, shape_desc=shape_desc)
#       plot(scaled_attention_logits, name="scaled_attention_logits", 
#            labels=labels, mask=orig_mask, shape_desc=shape_desc)
    
    
  # softmax is normalized on the last axis (seq_len_k) so that the scores
  # add up to 1.
  attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)  # (..., seq_len_q, seq_len_k)
  if draw:
    plot(attention_weights, name='attention_weights', labels=labels, 
         shape_desc=shape_desc)
    
#     plot(attention_weights, name='attention_weights', labels=labels, 
#          shape_desc=shape_desc,
#          mask=mask)
    
  
  if draw:
    plot(v, name='v', labels=['subwords in q', 'depth_v'], 
       shape_desc='\n(batch_size, seq_len_v, depth_v)')
  
  output = tf.matmul(attention_weights, v)  # (..., seq_len_q, depth_v)
  if draw:
    plot(output, name="output", labels=['subwords in q', 'depth_v'], 
         shape_desc='\n(batch_size, seq_len_q, depth_v)')

  return output, attention_weights