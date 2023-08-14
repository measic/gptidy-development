batch_size = 100
epochs = 100
samples = []
losses = []
saver = tf.train.Saver(var_list=g_vars)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for e in range(epochs):
        for ii in range(mnist.train.num_examples // batch_size):
            batch = mnist.train.next_batch(batch_size)
            batch_images = batch[0].reshape((batch_size, 784))
            batch_images = batch_images * 2 - 1
            variable_def = np.random.uniform(-1, 1, size=(batch_size, z_size))
            _ = sess.run(d_train_opt, feed_dict={input_real: batch_images, input_z: variable_def})
            _ = sess.run(g_train_opt, feed_dict={input_z: variable_def})
        train_loss_d = sess.run(d_loss, {input_z: variable_def, input_real: batch_images})
        train_loss_g = g_loss.eval({input_z: variable_def})
        print('Epoch {}/{}...'.format(e + 1, epochs), 'Discriminator Loss: {:.4f}...'.format(train_loss_d), 'Generator Loss: {:.4f}'.format(train_loss_g))
        losses.append((train_loss_d, train_loss_g))
        sample_z = np.random.uniform(-1, 1, size=(16, z_size))
        gen_samples = sess.run(generator(input_z, input_size, n_units=g_hidden_size, reuse=True, alpha=alpha), feed_dict={input_z: sample_z})
        samples.append(gen_samples)
        saver.save(sess, './checkpoints/generator.ckpt')
with open('train_samples.pkl', 'wb') as f:
    pkl.dump(samples, f)