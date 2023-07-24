# DL with inception.

from tensorflow.python.framework import ops
ops.reset_default_graph()

batch_size = 16
patch_size = 5
depth = 16
num_hidden_full_1 = 96
num_hidden_full_2 = 96

graph = tf.Graph()

with graph.as_default():

    # Input data.
    tf_train_dataset = tf.placeholder(
        tf.float32, shape=(batch_size, image_size, image_size, num_channels))
    tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, num_labels))
    tf_valid_dataset = tf.constant(valid_dataset)
    tf_test_dataset = tf.constant(test_dataset)
  
    # Variables.
    #layer1_weights = tf.Variable(tf.truncated_normal(
    #    [patch_size, patch_size, num_channels, depth], stddev=0.1))
    #layer1_biases = tf.Variable(tf.zeros([depth]))
    #layer2_weights = tf.Variable(tf.truncated_normal(
    #    [patch_size, patch_size, depth, depth], stddev=0.1))
    #layer2_biases = tf.Variable(tf.constant(1.0, shape=[depth]))
    # standard conv2d:
    # layer3_weights = tf.Variable(tf.truncated_normal(
    #     [image_size // 4 * image_size // 4 * depth, num_hidden_full_1], stddev=0.1))
    # inception is = [16, 28, 28, 64] reshaped (16, 50176)
    layer3_weights = init_weights([image_size * image_size * 64, num_hidden_full_1])
    layer3_biases = init_weights([num_hidden_full_1], method="ones")
    keep3 = tf.placeholder("float")
    layer4_weights = init_weights([num_hidden_full_1, num_hidden_full_2])
    layer4_biases = init_weights([num_hidden_full_2], method="ones")
    keep4 = tf.placeholder("float")
    layer5_weights = init_weights([num_hidden_full_2, num_labels])
    layer5_biases = init_weights([num_labels], method="ones")
    # vars for inception
    inception_1x1_weights = tf.Variable(tf.truncated_normal(
        [1, 1, num_channels, depth], stddev=0.1))
    inception_1x1_biases = tf.Variable(tf.zeros([depth]))
    pre_inception_1x1_weights = tf.Variable(tf.truncated_normal(
        [1, 1, num_channels, depth], stddev=0.1))
    pre_inception_1x1_biases = tf.Variable(tf.zeros([depth]))
    inception_1x1_pool_weights = tf.Variable(tf.truncated_normal(
        [1, 1, num_channels, depth], stddev=0.1))
    inception_1x1_pool_biases = tf.Variable(tf.zeros([depth]))
    inception_3x3_weights = tf.Variable(tf.truncated_normal(
        [3, 3, depth, depth], stddev=0.1))
    inception_3x3_biases = tf.Variable(tf.zeros([depth]))
    inception_5x5_weights = tf.Variable(tf.truncated_normal(
        [5, 5, depth, depth], stddev=0.1))
    inception_5x5_biases = tf.Variable(tf.zeros([depth]))

    def inception_layer(data):
        # Inception 1x1
        conv_1x1 = tf.nn.conv2d(data, inception_1x1_weights, [1, 1, 1, 1], padding='SAME')
        conv_1x1 = tf.nn.relu(conv_1x1 + inception_1x1_biases)
        print("1x1", conv_1x1.get_shape())
        ## 1x1 - before the bigger patches
        conv_pre = tf.nn.conv2d(data, pre_inception_1x1_weights, [1, 1, 1, 1], padding='SAME')
        conv_pre = tf.nn.relu(conv_pre + pre_inception_1x1_biases)
        # Pooling 3x3
        ## average pool followed by a 1x1
        conv_pool = tf.nn.avg_pool(data, [1, 3, 3, 1], [1, 1, 1, 1], padding='SAME')
        conv_pool = tf.nn.conv2d(conv_pool, inception_1x1_pool_weights, [1, 1, 1, 1], padding='SAME')
        conv_pool = tf.nn.relu(conv_pool + inception_1x1_pool_biases)
        print("pool", conv_pool.get_shape())
        # Inception 3x3
        ## 1x1 followed by a 3x3
        conv_3x3 = tf.nn.conv2d(conv_pre, inception_3x3_weights, [1, 1, 1, 1], padding='SAME')
        conv_3x3 = tf.nn.relu(conv_3x3 + inception_3x3_biases)
        print("3x3", conv_3x3.get_shape())
        # Inception 5x5
        ## 1x1 followed by a 5x5
        conv_5x5 = tf.nn.conv2d(conv_pre, inception_5x5_weights, [1, 1, 1, 1], padding='SAME')
        conv_5x5 = tf.nn.relu(conv_5x5 + inception_5x5_biases)
        print("5x5", conv_5x5.get_shape())
        inception_result = tf.concat(3, [conv_1x1, conv_3x3, conv_5x5, conv_pool])
        print(inception_result.get_shape())
        return inception_result

    # Model. using elu not relu.
    def model(data):
        # layer 1 convo. max_pool 2x2.
        #conv = tf.nn.conv2d(data, layer1_weights, [1, 1, 1, 1], padding='SAME')
        #pool = tf.nn.max_pool(conv, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        #hidden = tf.nn.elu(pool + layer1_biases)
        # layer 2 convo. max_pool 2x2
        #conv = tf.nn.conv2d(hidden, layer2_weights, [1, 1, 1, 1], padding='SAME')
        #pool = tf.nn.max_pool(conv, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        #hidden = tf.nn.elu(pool + layer2_biases)
        hidden = inception_layer(data)
        # layer 3 fully connected.
        shape = hidden.get_shape().as_list()
        reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
        hidden = tf.nn.elu(tf.matmul(reshape, layer3_weights) + layer3_biases)
        hidden = tf.nn.dropout(hidden, keep3)
        # layer 4 fully connected
        hidden = tf.nn.elu(tf.matmul(hidden, layer4_weights) + layer4_biases)
        hidden = tf.nn.dropout(hidden, keep4)
        # layer 5 output
        output = tf.matmul(hidden, layer5_weights) + layer5_biases
        return output
  
    # Training computation.
    logits = model(tf_train_dataset)
    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))
    
    # Optimizer.
    # optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)
    optimizer = tf.train.AdamOptimizer(1e-4).minimize(loss)
  
    # Predictions for the training, validation, and test data.
    train_prediction = tf.nn.softmax(logits)
    valid_prediction = tf.nn.softmax(model(tf_valid_dataset))
    test_prediction = tf.nn.softmax(model(tf_test_dataset))