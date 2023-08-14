optimizer = tf.train.GradientDescentOptimizer(0.0001)
model = two_layer_nn(output_size=1, loss_type='regression')
variable_def = 300
model.fit(X, y, optimizer, num_epochs=variable_def, track_accuracy=False)