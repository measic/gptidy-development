#padded too maxlen 25
maxlen = 25
padded_X = pad_sequences(trans_X, maxlen = maxlen, dtype = "uint32", padding = "post", truncating = "post", value = 0)
padded_T = pad_sequences(trans_T, maxlen = maxlen, dtype = "uint32", padding = "post", truncating = "post", value = 0)