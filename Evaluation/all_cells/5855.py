# define network parameters
y = tf.placeholder(tf.int32, shape=(None), name='y')
one_hot_y = tf.one_hot(y, 43)
x = tf.placeholder(tf.float32, shape=(None, 32, 32, 1), name='x')
mu, sigma, bias_value = 0, 0.1, 0.01
conv1_params = (5,5,1,6, 1, 'VALID')
conv2_params = (5, 5, 6, 16, 1, 'VALID')
p1_params = (2, 2, 'VALID')
p2_params = (2, 2, 'VALID')
fc1_params = 120
fc2_params = 84
fc3_params = 43
hold_prob = tf.placeholder(tf.float32, name='hold_prob')

# create the network
lenet = LeNet(x, mu, sigma, bias_value, conv1_params,
                  conv2_params, p1_params, p2_params, fc1_params,
                  fc2_params, fc3_params, hold_prob)