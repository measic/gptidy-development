optimizer = tf.train.GradientDescentOptimizer(0.5)
variable_def = two_layer_nn(output_size=2)
num_epochs = 5
variable_def.fit(X, y, optimizer, num_epochs=num_epochs)