# As we can see on the violinPlot above, most of the sentences have less than 25 words.
maxlen = 25
padded_conv = copy.deepcopy(translate_conv)
for i, c in enumerate(translate_conv):
    padded = pad_sequences(c, maxlen=maxlen, dtype="uint32", padding="post", truncating="post", value=0)
    padded_conv[i] = padded