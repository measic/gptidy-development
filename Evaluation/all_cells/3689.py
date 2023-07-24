#ignore
# 讀取之前建立的 mha 來保證每次的 mha 結果都一樣
d_model = 4
num_heads = 2
mha_weights_dir = os.path.join(output_dir, "demo_mha")
weight_names = [str(i) for i in range(8)]

mha = MultiHeadAttentionDemo(d_model, num_heads)
_, _ = mha(emb_inp, emb_inp, emb_inp, None)

if not os.path.exists(mha_weights_dir):
  os.makedirs(mha_weights_dir)

if not os.path.exists(os.path.join(mha_weights_dir, weight_names[0] + '.npy')):
  weights = mha.get_weights()
  for name, weight in zip(weight_names, weights):
    np.save(os.path.join(mha_weights_dir, name + '.npy'), weight)
else:
  weights = [np.load(os.path.join(mha_weights_dir, name + '.npy')) for name in weight_names]
  mha.set_weights(weights)

num_heads = 2
print(f"d_model: {d_model}")
print(f"num_heads: {num_heads}\n")

v = k = q = emb_inp
padding_mask = create_padding_mask(inp)
print("q.shape:", q.shape)
print("k.shape:", k.shape)
print("v.shape:", v.shape)
print("padding_mask.shape:", padding_mask.shape)

output, attention_weights = mha(v, k, q, mask)
print("output.shape:", output.shape)
print("attention_weights.shape:", attention_weights.shape)

print("\noutput:", output)