#ignore
def decode(batch, lang="en"):
  if lang == 'en':
    tokenizer = subword_encoder_en
  else:
    tokenizer = subword_encoder_zh

  result = []
  for e0 in range(batch.shape[0]):
    idx_sequence = batch[e0].numpy()
    sentence = []
    for idx in idx_sequence:
      if idx == 0:
        token = '<pad>'
      elif idx == tokenizer.vocab_size:
        token = '<start>'
      elif idx == tokenizer.vocab_size + 1:
        token = '<end>'
      else:
        token = tokenizer.decode([idx])
      sentence.append(token)
    result.append(sentence)
    
  return np.array(result)