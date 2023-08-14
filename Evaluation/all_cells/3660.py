#ignore
# 讀取之前建立的 emb layer 來保證每次的 emb_inp, emb_tar 結果都一樣
d_model = 4
vocab_size_en = subword_encoder_en.vocab_size + 2
vocab_size_zh = subword_encoder_zh.vocab_size + 2

emb_en_model_path = os.path.join(output_dir, "demo_emb_en_model.h5")
emb_zh_model_path = os.path.join(output_dir, "demo_emb_zh_model.h5")

# en
if not os.path.exists(emb_en_model_path):
  demo_emb_en_model = tf.keras.Sequential()
  demo_emb_en_model.add(tf.keras.layers.Embedding(vocab_size_en, d_model))
  demo_emb_en_model.save(emb_en_model_path)
  embedding_layer_en = demo_emb_en_model
else:
  embedding_layer_en = tf.keras.models.load_model(emb_en_model_path)
# zh
if not os.path.exists(emb_zh_model_path):
  demo_emb_zh_model = tf.keras.Sequential()
  demo_emb_zh_model.add(tf.keras.layers.Embedding(vocab_size_zh, d_model))
  demo_emb_zh_model.save(emb_zh_model_path)
  embedding_layer_zh = demo_emb_zh_model
else:
  embedding_layer_zh = tf.keras.models.load_model(emb_zh_model_path)
clear_output()