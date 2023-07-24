save_file= './train_model_best.ckpt'
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session, save_file)
    feed_dict = {tf_train_dataset : X2_norm, tf_keep_prob : 1}
    proba = session.run(train_prediction, feed_dict)