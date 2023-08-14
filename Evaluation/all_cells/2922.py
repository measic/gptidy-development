x0 = np.array([[1.], [1.]])  # 2x1 vector 

A = tf.constant(np.array([[1.001, 0], [0, -0.6]]), dtype=tf.float32, name='A')  # system dynamics
B = tf.constant(np.array([[1.], [1.]]), dtype=tf.float32, name='B')

Q = tf.constant([[1.,0.], [0.,1.]], name='Q')  # weighting
R = tf.constant(1., name='R')

x = tf.constant(x0, dtype=tf.float32, name="state")

T = 10