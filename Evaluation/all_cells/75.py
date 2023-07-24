with tf.Session() as sess:
    output = convolution.eval(feed_dict={X: images})