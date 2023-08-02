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
            variable_def = batch[0].reshape((batch_size, 784))
            variable_def = variable_def * 2 - 1
            batch_z = np.random.uniform(-1, 1, size=(batch_size, z_size))
            _ = sess.run(d_train_opt, feed_dict={input_real: variable_def, input_z: batch_z})
            _ = sess.run(g_train_opt, feed_dict={input_z: batch_z})
        train_loss_d = sess.run(d_loss, {input_z: batch_z, input_real: variable_def})
        train_loss_g = g_loss.eval({input_z: batch_z})
        print('Epoch {}/{}...'.format(e + 1, epochs), 'Discriminator Loss: {:.4f}...'.format(train_loss_d), 'Generator Loss: {:.4f}'.format(train_loss_g))
        losses.append((train_loss_d, train_loss_g))
        sample_z = np.random.uniform(-1, 1, size=(16, z_size))
        gen_samples = sess.run(generator(input_z, input_size, n_units=g_hidden_size, reuse=True, alpha=alpha), feed_dict={input_z: sample_z})
        samples.append(gen_samples)
        saver.save(sess, './checkpoints/generator.ckpt')
with open('train_samples.pkl', 'wb') as f:
    pkl.dump(samples, f)