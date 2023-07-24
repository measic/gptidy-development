### Define your architecture here.
### Feel free to use as many code cells as needed.
from tensorflow.contrib.layers import flatten

def LeNet(x):    
    # Arguments used for tf.truncated_normal, randomly defines variables for the weights and biases for each layer
    mu = 0
    sigma = 0.1
    
    # SOLUTION: Layer 1: Convolutional. Input = 32x32x3. Output = 28x28x6.
    conv1_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 3, 6), mean = mu, stddev = sigma))
    conv1_b = tf.Variable(tf.zeros(6))
    conv1   = tf.nn.conv2d(x, conv1_W, strides=[1, 1, 1, 1], padding='VALID') + conv1_b

    # SOLUTION: Activation.
    conv1 = tf.nn.relu(conv1)

    # SOLUTION: Pooling. Input = 28x28x6. Output = 14x14x6.
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # SOLUTION: Layer 2: Convolutional. Output = 10x10x16.
    conv2_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 6, 16), mean = mu, stddev = sigma))
    conv2_b = tf.Variable(tf.zeros(16))
    conv2   = tf.nn.conv2d(conv1, conv2_W, strides=[1, 1, 1, 1], padding='VALID') + conv2_b
    
    # SOLUTION: Activation.
    conv2 = tf.nn.relu(conv2)

    # SOLUTION: Pooling. Input = 10x10x16. Output = 5x5x16.
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # SOLUTION: Flatten. Input = 5x5x16. Output = 400.
    fc0   = flatten(conv2)
    
    # SOLUTION: Layer 3: Fully Connected. Input = 400. Output = 120.
    fc1_W = tf.Variable(tf.truncated_normal(shape=(400, 120), mean = mu, stddev = sigma))
    fc1_b = tf.Variable(tf.zeros(120))
    fc1   = tf.matmul(fc0, fc1_W) + fc1_b
    
    # SOLUTION: Activation.
    fc1    = tf.nn.relu(fc1)

    # SOLUTION: Layer 4: Fully Connected. Input = 120. Output = 84.
    fc2_W  = tf.Variable(tf.truncated_normal(shape=(120, 84), mean = mu, stddev = sigma))
    fc2_b  = tf.Variable(tf.zeros(84))
    fc2    = tf.matmul(fc1, fc2_W) + fc2_b
    
    # SOLUTION: Activation.
    fc2    = tf.nn.relu(fc2)

    # SOLUTION: Layer 5: Fully Connected. Input = 84. Output = 43.
    fc3_W  = tf.Variable(tf.truncated_normal(shape=(84, 43), mean = mu, stddev = sigma))
    fc3_b  = tf.Variable(tf.zeros(43))
    logits = tf.matmul(fc2, fc3_W) + fc3_b
    
    return logits

def model_arc(x):    
    # Arguments used for tf.truncated_normal, randomly defines variables for the weights and biases for each layer
    mu = 0
    sigma = 0.1
    
    # Layer 1: Convolutional. Input = 32x32x3. Output = 28x28x9.
    conv1_W = tf.Variable(tf.truncated_normal(shape=(5, 5, 3, 9), mean = mu, stddev = sigma))
    conv1_b = tf.Variable(tf.zeros(9))
    conv1   = tf.nn.bias_add(tf.nn.conv2d(x, conv1_W, strides=[1, 1, 1, 1], padding='VALID'), conv1_b)
    
    # Activation.
    conv1 = tf.nn.relu(conv1)
    
    # Pooling. Input = 28x28x9. Output = 14x14x9.
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    
    # Layer 2: Convolutional. Input = 14x14x9. Output = 12x12x27.
    conv2_W = tf.Variable(tf.truncated_normal(shape=(3, 3, 9, 27), mean = mu, stddev = sigma))
    conv2_b = tf.Variable(tf.zeros(27))
    conv2   = tf.nn.bias_add(tf.nn.conv2d(conv1, conv2_W, strides=[1, 1, 1, 1], padding='VALID'), conv2_b)
    
    # Activation.
    conv2 = tf.nn.relu(conv2)
    
    # Pooling. Input = 12x12x9. Output = 6x6x9.
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')
    
    # Layer 3: Convolutional. Input = 6x6x27. Output = 6x6x81.
    conv3_W = tf.Variable(tf.truncated_normal(shape=(1, 1, 27, 81), mean = mu, stddev = sigma))
    conv3_b = tf.Variable(tf.zeros(81))
    conv3   = tf.nn.bias_add(tf.nn.conv2d(conv2, conv3_W, strides=[1, 1, 1, 1], padding='VALID'), conv3_b)
    
    # Activation.
    conv3 = tf.nn.relu(conv3)
    
    # Dropout
    conv3 = tf.nn.dropout(conv3, keep_prob=0.5)
    
    # Activation.
    conv3 = tf.nn.relu(conv3)
    
    # Flatten. Input = 6x6x81. Output = 2916.
    fc0   = flatten(conv3)
    
    # Layer 4: Fully Connected. Input = 2916. Output = 972.
    fc1_W = tf.Variable(tf.truncated_normal(shape=(2916, 972), mean = mu, stddev = sigma))
    fc1_b = tf.Variable(tf.zeros(972))
    fc1   = tf.nn.xw_plus_b(fc0, fc1_W, fc1_b)
    
    # Activation.
    fc1    = tf.nn.relu(fc1)

    # Layer 5: Fully Connected. Input = 972. Output = 324.
    fc2_W  = tf.Variable(tf.truncated_normal(shape=(972, 324), mean = mu, stddev = sigma))
    fc2_b  = tf.Variable(tf.zeros(324))
    fc2    = tf.nn.xw_plus_b(fc1, fc2_W, fc2_b)
    
    # Activation.
    fc2 = tf.nn.relu(fc2)

    # Layer 6: Fully Connected. Input = 324. Output = 108.
    fc3_W  = tf.Variable(tf.truncated_normal(shape=(324, 108), mean = mu, stddev = sigma))
    fc3_b  = tf.Variable(tf.zeros(108))
    fc3 = tf.nn.xw_plus_b(fc2, fc3_W, fc3_b)
    
    # Activation.
    fc3 = tf.nn.relu(fc3)

    # Layer 7: Fully Connected. Input = 108. Output = 43.
    fc4_W  = tf.Variable(tf.truncated_normal(shape=(108, 43), mean = mu, stddev = sigma))
    fc4_b  = tf.Variable(tf.zeros(43))
    logits = tf.nn.xw_plus_b(fc3, fc4_W, fc4_b)
    
    return logits