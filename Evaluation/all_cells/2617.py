%%time
# posterior inference
M = 300
mu_2_sample, sigmasq_2_sample, pi_2_sample = qmu_2.sample(M), qsigma_2.sample(M), qpi_2.sample(M)
x_2_post = Normal(loc=tf.ones([N, 1, 1, 1]) * mu_2_sample, scale=tf.ones([N, 1, 1, 1]) * tf.sqrt(sigmasq_2_sample))
x_2_broadcasted = tf.cast(tf.tile(tf.reshape(X, [N, 1, 1, D]), [1, M, K, 1]), dtype=tf.float32)
log_liks_2 = tf.reduce_mean(tf.reduce_sum(x_2_post.log_prob(x_2_broadcasted), 3), 1)
clusters_2 = tf.argmax(log_liks_2, 1).eval()
posterior_mu_2 = qmu_2.params.eval().mean(axis=0)