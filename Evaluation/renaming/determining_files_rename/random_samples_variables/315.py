X = tf.placeholder(tf.float32, shape=(None, height, width, channels))
max_pool = tf.nn.max_pool(X, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
with tf.Session() as sess:
    variable_def = sess.run(max_pool, feed_dict={X: dataset})
plt.imshow(variable_def[0].astype(np.uint8))
plt.show()