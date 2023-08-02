variable_def = tf.placeholder(tf.float32, shape=(None, height, width, channels))
max_pool = tf.nn.max_pool(variable_def, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
with tf.Session() as sess:
    output = sess.run(max_pool, feed_dict={variable_def: dataset})
plt.imshow(output[0].astype(np.uint8))
plt.show()