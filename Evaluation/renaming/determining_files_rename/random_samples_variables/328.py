my_labels = [16, 33, 11, 38, 35, 17]
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.import_meta_graph('./lenet.meta')
    saver.restore(sess, './lenet')
    my_images_normalized = [normalize(rgb2gray(img)) for img in my_images]
    variable_def = evaluate(my_images_normalized, my_labels)
    print('Test Set Accuracy = {:.3f}'.format(variable_def))