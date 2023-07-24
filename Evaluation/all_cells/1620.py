tf.reset_default_graph()

nb_neurons_input = 4  # len(obs)
nb_neurons_hidden_layer = 4
nb_neurons_output = 1

X = tf.placeholder(shape=[None, nb_neurons_input], dtype=tf.float32, name="X")

with tf.name_scope("dnn"): 
    initializer_w = tf.contrib.layers.xavier_initializer()
    initializer_b = tf.zeros_initializer() 
    hidden = tf.layers.dense(X, nb_neurons_hidden_layer, \
                             activation=tf.nn.elu, \
                             kernel_initializer=tf.contrib.layers.xavier_initializer(), \
                             name="hidden")
    output = tf.layers.dense(hidden, nb_neurons_output, 
                             activation=tf.nn.sigmoid,
                             name="output")  # proba of moving kart to left

init = tf.global_variables_initializer()