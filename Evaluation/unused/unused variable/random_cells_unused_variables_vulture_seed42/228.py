save_file= './train_model_best.ckpt'
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session, save_file)
    feed_dict = {tf_train_dataset : X2_norm, tf_keep_prob : 1}
    logi = session.run(logits, feed_dict)
    predicts = session.run(tf.nn.top_k(logi, k=5, sorted=True))
    proba = session.run(tf.nn.softmax(predicts[0]))