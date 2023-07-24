# Numpy arrays to tensors
X = tf.constant(X)
y = tf.constant(y)
y = tf.reshape(y, [-1, 1])  # change from row vector to column vector