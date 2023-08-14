from tensorflow.contrib.layers import flatten

def LeNet(x):
    mu = 0
    sigma = 0.1
    conv1_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 3, 6), mean=mu, stddev=sigma))
    conv1_b = tf.Variable(tf.zeros(6))
    conv1 = tf.nn.conv2d(x, conv1_W, strides=[1, 1, 1, 1], padding='VALID') + conv1_b
    conv1 = tf.nn.relu(conv1)
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    conv2_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 6, 16), mean=mu, stddev=sigma))
    conv2_b = tf.Variable(tf.zeros(16))
    conv2 = tf.nn.conv2d(conv1, conv2_W, strides=[1, 1, 1, 1], padding='VALID') + conv2_b
    conv2 = tf.nn.relu(conv2)
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    fc0 = flatten(conv2)
    fc1_W = tf.Variable(tf.truncated_normal(shape=(400, 120), mean=mu, stddev=sigma))
    fc1_b = tf.Variable(tf.zeros(120))
    fc1 = tf.matmul(fc0, fc1_W) + fc1_b
    fc1 = tf.nn.relu(fc1)
    fc2_W = tf.Variable(tf.truncated_normal(shape=(120, 84), mean=mu, stddev=sigma))
    fc2_b = tf.Variable(tf.zeros(84))
    fc2 = tf.matmul(fc1, fc2_W) + fc2_b
    fc2 = tf.nn.relu(fc2)
    fc3_W = tf.Variable(tf.truncated_normal(shape=(84, 43), mean=mu, stddev=sigma))
    fc3_b = tf.Variable(tf.zeros(43))
    logits = tf.matmul(fc2, fc3_W) + fc3_b
    return logits

def model_arc(x):
    mu = 0
    sigma = 0.1
    conv1_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 3, 9), mean=mu, stddev=sigma))
    conv1_b = tf.Variable(tf.zeros(9))
    conv1 = tf.nn.bias_add(tf.nn.conv2d(x, conv1_W, strides=[1, 1, 1, 1], padding='VALID'), conv1_b)
    conv1 = tf.nn.relu(conv1)
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    conv2_W = tf.Variable(tf.truncated_normal(shape=(3, 3, 9, 27), mean=mu, stddev=sigma))
    conv2_b = tf.Variable(tf.zeros(27))
    conv2 = tf.nn.bias_add(tf.nn.conv2d(conv1, conv2_W, strides=[1, 1, 1, 1], padding='VALID'), conv2_b)
    conv2 = tf.nn.relu(conv2)
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    conv3_W = tf.Variable(tf.truncated_normal(shape=(1, 1, 27, 81), mean=mu, stddev=sigma))
    conv3_b = tf.Variable(tf.zeros(81))
    conv3 = tf.nn.bias_add(tf.nn.conv2d(conv2, conv3_W, strides=[1, 1, 1, 1], padding='VALID'), conv3_b)
    conv3 = tf.nn.relu(conv3)
    conv3 = tf.nn.dropout(conv3, keep_prob=0.5)
    conv3 = tf.nn.relu(conv3)
    fc0 = flatten(conv3)
    fc1_W = tf.Variable(tf.truncated_normal(shape=(2916, 972), mean=mu, stddev=sigma))
    fc1_b = tf.Variable(tf.zeros(972))
    fc1 = tf.nn.xw_plus_b(fc0, fc1_W, fc1_b)
    fc1 = tf.nn.relu(fc1)
    fc2_W = tf.Variable(tf.truncated_normal(shape=(972, 324), mean=mu, stddev=sigma))
    fc2_b = tf.Variable(tf.zeros(324))
    fc2 = tf.nn.xw_plus_b(fc1, fc2_W, fc2_b)
    fc2 = tf.nn.relu(fc2)
    fc3_W = tf.Variable(tf.truncated_normal(shape=(324, 108), mean=mu, stddev=sigma))
    fc3_b = tf.Variable(tf.zeros(108))
    variable_def = tf.nn.xw_plus_b(fc2, fc3_W, fc3_b)
    variable_def = tf.nn.relu(variable_def)
    fc4_W = tf.Variable(tf.truncated_normal(shape=(108, 43), mean=mu, stddev=sigma))
    fc4_b = tf.Variable(tf.zeros(43))
    logits = tf.nn.xw_plus_b(variable_def, fc4_W, fc4_b)
    return logits