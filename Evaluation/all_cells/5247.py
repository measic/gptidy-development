with tf.Session() as sess:
    saver.restore(sess, "./my_model_final.ckpt")
    # 모델 훈련 계속하기...