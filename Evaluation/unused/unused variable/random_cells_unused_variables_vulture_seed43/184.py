# Input placehodlers
# N_INPUT -> size of vector representing one image in sequence
# Inputs shape (batch_size, max_seq_length, vec_size) - time major
inputs = tf.placeholder(shape=(None, None, N_INPUT),
                                dtype=tf.float32,
                                name='inputs')
length = tf.placeholder(shape=(None,),
                        dtype=tf.int32,
                        name='length')
# Required for training, not required for application
targets = tf.placeholder(shape=(None, None),
                         dtype=tf.int64,
                         name='targets')
# Dropout value
keep_prob = tf.placeholder(tf.float32, name='keep_prob')