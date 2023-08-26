softmax_logits = tf.nn.softmax(logits)
top_k = tf.nn.top_k(softmax_logits, k=3)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.import_meta_graph('./lenet.meta')
    saver.restore(sess, './lenet')
    batch_x = np.expand_dims(my_images_normalized, axis=3)
    sample_softmax_logits = sess.run(softmax_logits, feed_dict={x: batch_x, keep_prob: 1.0})
    my_top_k = sess.run(top_k, feed_dict={x: batch_x, keep_prob: 1.0})
    fig, axs = plt.subplots(len(my_images), 1, figsize=(20, 25))
    fig.subplots_adjust(hspace=1.0, wspace=0.6)
    axs = axs.ravel()
    for i, image in enumerate(my_images):
        axs[i].axis('off')
        axs[i].imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
        guess1 = my_top_k[1][i][0]
        index1 = np.argwhere(y_valid == guess1)[0]
        guess2 = my_top_k[1][i][1]
        index2 = np.argwhere(y_valid == guess2)[0]
        variable_def = my_top_k[1][i][2]
        index3 = np.argwhere(y_valid == variable_def)[0]
        title = ''
        title += 'guess 1: class ' + sign_dict[str(guess1)] + ', probability: ' + str(100 * my_top_k[0][i][0]) + '\n'
        title += 'guess 2: class ' + sign_dict[str(guess2)] + ', probability: ' + str(100 * my_top_k[0][i][1]) + '\n'
        title += 'guess 3: class ' + sign_dict[str(variable_def)] + ', probability: ' + str(100 * my_top_k[0][i][2])
        axs[i].set_title(title)