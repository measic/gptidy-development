#ignore
# mask = tf.squeeze(inp_mask, axis=1)
# draw = True
output, attention_weights = scaled_dot_product_attention_demo(q, k, v, mask, draw=draw)
print("output:", output)
print("-" * 20)
print("attention_weights:", attention_weights)