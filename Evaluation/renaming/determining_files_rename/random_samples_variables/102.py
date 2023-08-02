from tensorflow.python.framework import ops
ops.reset_default_graph()
batch_size = 16
patch_size = 5
depth = 16
num_hidden_full_1 = 512
num_hidden_full_2 = 64

def init_weights(shape, method='xavier'):
    if method == 'zeros':
        return tf.Variable(tf.zeros(shape, dtype=tf.float32))
    elif method == 'ones':
        return tf.Variable(tf.ones(shape, dtype=tf.float32))
    elif method == 'uniform':
        return tf.Variable(tf.random_normal(shape, stddev=0.01, dtype=tf.float32))
    elif method == 'altxavier':
        low = -4 * np.sqrt(6.0 / (shape[0] + shape[1]))
        high = 4 * np.sqrt(6.0 / (shape[0] + shape[1]))
        return tf.Variable(tf.random_uniform(shape, minval=low, maxval=high, dtype=tf.float32))
    elif method == 'xavier':
        sd = np.sqrt(3.0 / (shape[0] + shape[1]))
        return tf.Variable(tf.truncated_normal(shape, stddev=sd))
    else:
        sd = np.sqrt(2.0 / shape[0])
        return tf.Variable(tf.truncated_normal(shape, stddev=sd))
graph = tf.Graph()
with graph.as_default():
    variable_def = tf.placeholder(tf.float32, shape=(batch_size, image_size, image_size, num_channels))
    tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, num_labels))
    tf_valid_dataset = tf.constant(valid_dataset)
    tf_test_dataset = tf.constant(test_dataset)
    layer1_weights = tf.Variable(tf.truncated_normal([patch_size, patch_size, num_channels, depth], stddev=0.1))
    layer1_biases = tf.Variable(tf.zeros([depth]))
    layer2_weights = tf.Variable(tf.truncated_normal([patch_size, patch_size, depth, depth * 2], stddev=0.1))
    layer2_biases = tf.Variable(tf.constant(1.0, shape=[depth * 2]))
    layer3_weights = init_weights([image_size // 4 * image_size // 4 * depth * 2, num_hidden_full_1])
    layer3_biases = init_weights([num_hidden_full_1], method='ones')
    keep3 = tf.placeholder('float')
    layer4_weights = init_weights([num_hidden_full_1, num_hidden_full_2])
    layer4_biases = init_weights([num_hidden_full_2], method='ones')
    keep4 = tf.placeholder('float')
    layer5_weights = init_weights([num_hidden_full_2, num_labels])
    layer5_biases = init_weights([num_labels], method='ones')

    def model(data):
        conv = tf.nn.conv2d(data, layer1_weights, [1, 1, 1, 1], padding='SAME')
        conv = tf.nn.elu(conv + layer1_biases)
        hidden = tf.nn.max_pool(conv, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv = tf.nn.conv2d(hidden, layer2_weights, [1, 1, 1, 1], padding='SAME')
        conv = tf.nn.elu(conv + layer2_biases)
        hidden = tf.nn.max_pool(conv, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        shape = hidden.get_shape().as_list()
        reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
        hidden = tf.nn.elu(tf.matmul(reshape, layer3_weights) + layer3_biases)
        hidden = tf.nn.dropout(hidden, keep3)
        hidden = tf.nn.elu(tf.matmul(hidden, layer4_weights) + layer4_biases)
        hidden = tf.nn.dropout(hidden, keep4)
        output = tf.matmul(hidden, layer5_weights) + layer5_biases
        return output
    logits = model(variable_def)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))
    optimizer = tf.train.AdamOptimizer(0.0001).minimize(loss)
    train_prediction = tf.nn.softmax(logits)
    valid_prediction = tf.nn.softmax(model(tf_valid_dataset))
    test_prediction = tf.nn.softmax(model(tf_test_dataset))