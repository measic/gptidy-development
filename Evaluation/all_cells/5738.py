def define_graph():
    
    tf_train_dataset = tf.placeholder(tf.float32, 
                          shape=[None, image_size, image_size, num_channels])
    tf_train_labels = tf.placeholder(tf.float32, 
                          shape=[None, n_classes])
    tf_train_labels_cls = tf.argmax(tf_train_labels, dimension=1)

    tf_beta = tf.placeholder(tf.float32)
    tf_keep_prob = tf.placeholder(tf.float32)
    tf_learning_rate = tf.placeholder(tf.float32)

    layer_width = {
        'layer_1': 48,
        'layer_2': 64,
        'layer_3': 128,
        'fc1': 512,
        'fc2': 512
    }

    weights = {
        'layer_1': create_conv_weight(input_feature_map = num_channels, output_feature_map = layer_width['layer_1']
                                      , filter_height = 3, filter_width = 3, weight_name = 'W_L1'),

        'layer_2': create_conv_weight(input_feature_map = layer_width['layer_1'], output_feature_map = layer_width['layer_2']
                                      , filter_height = 3, filter_width = 3, weight_name = 'W_L2'),

        'layer_3': create_conv_weight(input_feature_map = layer_width['layer_2'], output_feature_map = layer_width['layer_3']
                                      , filter_height = 3, filter_width = 3, weight_name = 'W_L3'),

        'fc1': create_fc_weight(input_feature_map = 2048, output_feature_map = layer_width['fc1']
                                    , weight_name = 'W_F1'),

        'fc2': create_fc_weight(input_feature_map = layer_width['fc1'], output_feature_map = layer_width['fc2']
                                    , weight_name = 'W_F2'),

        'out': create_fc_weight(input_feature_map = layer_width['fc2'], output_feature_map = n_classes
                                    , weight_name = 'W_out')
    }

    biases = {
        'layer_1': tf.Variable(tf.constant(0.0, shape=[layer_width['layer_1']]), name='b_L1'),
        'layer_2': tf.Variable(tf.constant(0.0, shape=[layer_width['layer_2']]), name='b_L2'),
        'layer_3': tf.Variable(tf.constant(0.0, shape=[layer_width['layer_3']]), name='b_L3'),
        'fc1': tf.Variable(tf.constant(0.0, shape=[layer_width['fc1']]), name='b_F1'),
        'fc2': tf.Variable(tf.constant(0.0, shape=[layer_width['fc2']]), name='b_F2'),
        'out': tf.Variable(tf.constant(0.0, shape=[n_classes]), name='b_out')
    }

    # Layer 1
    conv1 = conv2d(tf_train_dataset, weights['layer_1'], biases['layer_1'], is_relu = True)
    conv1 = maxpool2d(conv1)
    #conv1_drop = tf.nn.dropout(conv1, tf_keep_prob)
    #print(conv1)

    # Layer 2
    conv2 = conv2d(conv1, weights['layer_2'], biases['layer_2'], is_relu = True)
    conv2 = maxpool2d(conv2)
    #conv2_drop = tf.nn.dropout(conv2, tf_keep_prob)
    #print('conv2')
    #print(conv2)

    # Layer 3
    conv3 = conv2d(conv2, weights['layer_3'], biases['layer_3'], is_relu = True)
    conv3 = maxpool2d(conv3)
    conv3_drop = tf.nn.dropout(conv3, tf_keep_prob)
    #print('conv3')
    #print(conv3)

    # Flatten
    flat, num_fc_layers = flatten_layer(conv3_drop)

    # Fully connected layer
    fc1 = tf.add(tf.matmul(flat, weights['fc1']), biases['fc1'])
    fc1 = tf.nn.relu(fc1)
    fc1 = tf.nn.dropout(fc1, tf_keep_prob)
    #print(fc1)

    fc2 = tf.add(tf.matmul(fc1, weights['fc2']), biases['fc2'])
    fc2 = tf.nn.relu(fc2)
    fc2 = tf.nn.dropout(fc2, tf_keep_prob)
    #print(fc2)

    # Output Layer - class prediction
    logits = tf.add(tf.matmul(fc2, weights['out']), biases['out'], name='logits')
    train_prediction = tf.nn.softmax(logits) 

    regularizers = (tf.nn.l2_loss(weights['layer_1']) 
                + tf.nn.l2_loss(weights['layer_2']) 
                + tf.nn.l2_loss(weights['layer_3']) 
                + tf.nn.l2_loss(weights['fc1'])
                + tf.nn.l2_loss(weights['fc2'])
                + tf.nn.l2_loss(weights['out']))

    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits,
                                                    labels=tf_train_labels)

    loss = tf.reduce_mean(cross_entropy) + tf_beta*regularizers 
    tf.summary.scalar('loss', loss) 

    with tf.name_scope('SGD'):
        optimizer = tf.train.AdamOptimizer(learning_rate=tf_learning_rate).minimize(loss) #AdamOptimizer #GradientDescentOptimizer

    with tf.name_scope('accuracy'):
        with tf.name_scope('correct_prediction'):

          labels_pred_cls = tf.argmax(train_prediction,dimension = 1) 
          correct_prediction = tf.equal(labels_pred_cls, tf_train_labels_cls)

        with tf.name_scope('accuracy'):
          accuracy_operation = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
          tf.summary.scalar('accuracy', accuracy_operation) 

    summary_op = tf.summary.merge_all()
    
    return tf_train_dataset, tf_train_labels, tf_train_labels_cls, tf_beta, tf_keep_prob, tf_learning_rate, weights, biases,conv1, conv2, conv3, flat, fc1, fc2, logits, train_prediction, regularizers,  cross_entropy, loss, optimizer, labels_pred_cls, correct_prediction, accuracy_operation, accuracy_operation, summary_op  
  