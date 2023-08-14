T = 1000  # number of MCMC samples
with tf.name_scope("posterior_2"):
    qpi_2 = Empirical(tf.get_variable("qpi_2/params", [T, K], initializer=tf.constant_initializer(1.0/K)))
    qmu_2 = Empirical(tf.get_variable("qmu_2/params", [T, K, D], initializer=tf.zeros_initializer()))
    qsigma_2 = Empirical(tf.get_variable("qsigma_2/params", [T, K, D], initializer=tf.ones_initializer()))
    qz_2 = Empirical(tf.get_variable("qz_2/params", [T, N], initializer=tf.zeros_initializer(), dtype=tf.int32))