variable_def = tf.train.GradientDescentOptimizer(0.5)
model = two_layer_nn(output_size=2)
num_epochs = 5
model.fit(X, y, variable_def, num_epochs=num_epochs)