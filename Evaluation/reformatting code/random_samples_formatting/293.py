with tf.Session(graph=graph) as sess:
   
    #saver.restore(sess, "./model/lr_0.003")
    saver.restore(sess, tf.train.latest_checkpoint('./model'))
    result = sess.run(tf.argmax(y_pred, 1), feed_dict={x:test_images_np_gray, hold_prob:1.0})