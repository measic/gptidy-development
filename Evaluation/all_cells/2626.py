%%time
# MCMC
log_liks_3 = tf.reduce_sum(x_2_post.log_prob(x_2_broadcasted), 3)
pi_samples_tiled_3 = tf.tile(tf.expand_dims(tf.log(pi_2_sample), 0), [N, 1, 1])
sum_log_pi_normal_3 = tf.add(pi_samples_tiled_3, log_liks_3)
x_max_3 = tf.reduce_max(sum_log_pi_normal_3, axis=2)
edited_log_sum_3 = tf.add(x_max_3, tf.log(tf.reduce_sum(tf.exp(sum_log_pi_normal_3 -tf.expand_dims(x_max_3, 2)), axis=2)))
pdi_mean, pdi_variance = tf.nn.moments(tf.exp(edited_log_sum_3), axes=[1])
pdi = tf.divide(pdi_variance, pdi_mean)
wapdi_mean, wapdi_variance = tf.nn.moments(edited_log_sum_3, axes=[1])
wapdi_log_mean = tf.log(pdi_mean)
wapdi = tf.divide(wapdi_variance, wapdi_log_mean)
pdi_log = tf.divide(wapdi_variance, wapdi_mean)
pdi_mcmc, pdi_log_mcmc, wapdi_mcmc = sess.run([pdi, pdi_log, wapdi])