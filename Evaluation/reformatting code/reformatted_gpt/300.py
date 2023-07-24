# Edward model
cluster_means_tf = tf.convert_to_tensor(np.asarray(cluster_means), dtype=tf.float32)

with tf.name_scope("model_ed2"):
    pi_ed2 = Dirichlet(concentration=tf.constant([1.0] * K, name="pi/weights"), name="pi")
    mu_ed2 = Normal(loc=cluster_means_tf, scale=tf.ones(D, name="centroids/scale") * 20, name="centroids")
    sigmasq_ed2 = InverseGamma(concentration=tf.ones(D, name="variability/concentration"),
                               rate=tf.ones(D, name="variability/rate"), sample_shape=K, name="variability")
    x_ed2 = ParamMixture(pi_ed2, {'loc': mu_ed2, 'scale_diag': tf.sqrt(sigmasq_ed2)},
                         MultivariateNormalDiag, sample_shape=N, name="mixture")
    z_ed2 = x_ed2.cat