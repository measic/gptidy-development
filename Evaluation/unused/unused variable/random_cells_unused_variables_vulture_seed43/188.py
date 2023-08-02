T = 1000  # number of samples
with tf.name_scope("posterior"):
    qpi = Empirical(tf.get_variable("qpi/params", [T, K],initializer=tf.constant_initializer(1.0/K)))
    qmu = Empirical(tf.get_variable("qmu/params", [T, K, D],initializer=tf.zeros_initializer()))
    qsigma = Empirical(tf.get_variable("qsigma/params", [T, K, D],initializer=tf.ones_initializer()))
    qz = Empirical(tf.get_variable("qz/params", [T, N],initializer=tf.zeros_initializer(),dtype=tf.int32))