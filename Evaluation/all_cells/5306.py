clip_all_weights = tf.get_collection("max_norm")

with tf.Session() as sess:
    init.run()
    for epoch in range(n_epochs):
        for X_batch, y_batch in shuffle_batch(X_train, y_train, batch_size):
            sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
            sess.run(clip_all_weights)
        accuracy_val = accuracy.eval(feed_dict={X: X_valid, y: y_valid}) # 책에는 없음
        print(epoch, "검증 세트 정확도:", accuracy_val)                      # 책에는 없음

    save_path = saver.save(sess, "./my_model_final.ckpt")                # 책에는 없음