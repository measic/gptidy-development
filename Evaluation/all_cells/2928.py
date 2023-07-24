with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        sess.run(train, feed_dict={input_layer : x0.T})
        if i % 100 == 0:
            results = sess.run([xs, us, loss], feed_dict={input_layer : x0.T})
            labels  = "xs us loss".split(' ')
            print('training iteration', i)
            for label,result in zip(*(labels,results)) :
                print(label)
                print(result)
                print('')
            print('gradients')
            for g, v in grads_and_vars:
                print(str(sess.run(g, feed_dict={input_layer : x0.T})) + " - " + v.name)
            print('----------------------')