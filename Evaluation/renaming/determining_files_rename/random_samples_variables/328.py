my_labels = [16, 33, 11, 38, 35, 17]
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.import_meta_graph('./lenet.meta')
    saver.restore(sess, './lenet')
    variable_def = [normalize(rgb2gray(img)) for img in my_images]
    my_accuracy = evaluate(variable_def, my_labels)
    print('Test Set Accuracy = {:.3f}'.format(my_accuracy))