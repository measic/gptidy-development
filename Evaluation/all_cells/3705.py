#ignore
# labels = ['sentence', 'subword']
# # plot(inp, name='inp', labels=labels, shape_desc='(batch_size, inp_seq_len)')
# # plot(tar, name='tar', labels=labels, shape_desc='(batch_size, tar_seq_len)')

# # string
# plot(decode(inp), name='inp', is_string=True, 
#      labels=labels)
# plot(decode(tar, lang='zh'), name='tar', is_string=True, 
#      labels=labels)
# plot(decode(tar[:, :-1], lang='zh'), name='tar[:, :-1]', is_string=True, 
#      labels=labels)
# plot(decode(tar[:, 1:], lang='zh'), name='tar[:, 1:]', is_string=True, 
#      labels=labels)


# predicted_indices = tf.argmax(predictions, axis=-1)
# predicted_words = decode(predicted_indices, lang="zh")


# plot(predicted_words, name='predicted_words', is_string=True, 
#      labels=labels)