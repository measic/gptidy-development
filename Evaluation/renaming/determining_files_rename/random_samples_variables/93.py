from tensorflow.python.framework import ops
ops.reset_default_graph()
batch_size = 16
patch_size = 5
depth = 16
num_hidden_full_1 = 96
num_hidden_full_2 = 96
graph = tf.Graph()
with graph.as_default():
    tf_train_dataset = tf.placeholder(tf.float32, shape=(batch_size, image_size, image_size, num_channels))
    tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, num_labels))
    tf_valid_dataset = tf.constant(valid_dataset)
    tf_test_dataset = tf.constant(test_dataset)
    layer3_weights = init_weights([image_size * image_size * 64, num_hidden_full_1])
    layer3_biases = init_weights([num_hidden_full_1], method='ones')
    keep3 = tf.placeholder('float')
    layer4_weights = init_weights([num_hidden_full_1, num_hidden_full_2])
    layer4_biases = init_weights([num_hidden_full_2], method='ones')
    keep4 = tf.placeholder('float')
    layer5_weights = init_weights([num_hidden_full_2, num_labels])
    layer5_biases = init_weights([num_labels], method='ones')
    inception_1x1_weights = tf.Variable(tf.truncated_normal([1, 1, num_channels, depth], stddev=0.1))
    inception_1x1_biases = tf.Variable(tf.zeros([depth]))
    pre_inception_1x1_weights = tf.Variable(tf.truncated_normal([1, 1, num_channels, depth], stddev=0.1))
    pre_inception_1x1_biases = tf.Variable(tf.zeros([depth]))
    inception_1x1_pool_weights = tf.Variable(tf.truncated_normal([1, 1, num_channels, depth], stddev=0.1))
    inception_1x1_pool_biases = tf.Variable(tf.zeros([depth]))
    inception_3x3_weights = tf.Variable(tf.truncated_normal([3, 3, depth, depth], stddev=0.1))
    inception_3x3_biases = tf.Variable(tf.zeros([depth]))
    inception_5x5_weights = tf.Variable(tf.truncated_normal([5, 5, depth, depth], stddev=0.1))
    inception_5x5_biases = tf.Variable(tf.zeros([depth]))

    def inception_layer(data):
        conv_1x1 = tf.nn.conv2d(data, inception_1x1_weights, [1, 1, 1, 1], padding='SAME')
        conv_1x1 = tf.nn.relu(conv_1x1 + inception_1x1_biases)
        print('1x1', conv_1x1.get_shape())
        variable_def = tf.nn.conv2d(data, pre_inception_1x1_weights, [1, 1, 1, 1], padding='SAME')
        variable_def = tf.nn.relu(variable_def + pre_inception_1x1_biases)
        conv_pool = tf.nn.avg_pool(data, [1, 3, 3, 1], [1, 1, 1, 1], padding='SAME')
        conv_pool = tf.nn.conv2d(conv_pool, inception_1x1_pool_weights, [1, 1, 1, 1], padding='SAME')
        conv_pool = tf.nn.relu(conv_pool + inception_1x1_pool_biases)
        print('pool', conv_pool.get_shape())
        conv_3x3 = tf.nn.conv2d(variable_def, inception_3x3_weights, [1, 1, 1, 1], padding='SAME')
        conv_3x3 = tf.nn.relu(conv_3x3 + inception_3x3_biases)
        print('3x3', conv_3x3.get_shape())
        conv_5x5 = tf.nn.conv2d(variable_def, inception_5x5_weights, [1, 1, 1, 1], padding='SAME')
        conv_5x5 = tf.nn.relu(conv_5x5 + inception_5x5_biases)
        print('5x5', conv_5x5.get_shape())
        inception_result = tf.concat(3, [conv_1x1, conv_3x3, conv_5x5, conv_pool])
        print(inception_result.get_shape())
        return inception_result

    def model(data):
        hidden = inception_layer(data)
        shape = hidden.get_shape().as_list()
        reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
        hidden = tf.nn.elu(tf.matmul(reshape, layer3_weights) + layer3_biases)
        hidden = tf.nn.dropout(hidden, keep3)
        hidden = tf.nn.elu(tf.matmul(hidden, layer4_weights) + layer4_biases)
        hidden = tf.nn.dropout(hidden, keep4)
        output = tf.matmul(hidden, layer5_weights) + layer5_biases
        return output
    logits = model(tf_train_dataset)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))
    optimizer = tf.train.AdamOptimizer(0.0001).minimize(loss)
    train_prediction = tf.nn.softmax(logits)
    valid_prediction = tf.nn.softmax(model(tf_valid_dataset))
    test_prediction = tf.nn.softmax(model(tf_test_dataset))