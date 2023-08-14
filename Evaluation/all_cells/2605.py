%%time
M = 300 # posterior samples
mu_sample, sigmasq_sample, pi_sample = qmu.sample(M), qsigma.sample(M), qpi.sample(M)
x_post = Normal(loc=tf.ones([N, 1, 1, 1]) * mu_sample, scale=tf.ones([N, 1, 1, 1]) * tf.sqrt(sigmasq_sample))
x_broadcasted = tf.cast(tf.tile(tf.reshape(X, [N, 1, 1, D]), [1, M, K, 1]), dtype=tf.float32)
log_liks = tf.reduce_mean(tf.reduce_sum(x_post.log_prob(x_broadcasted), 3), 1)
clusters = tf.argmax(log_liks, 1).eval()
posterior_mu = qmu.params.eval().mean(axis=0)