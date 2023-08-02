variable_def = tf.train.GradientDescentOptimizer(0.0001)
model = two_layer_nn(output_size=1, loss_type='regression')
num_epochs = 300
model.fit(X, y, variable_def, num_epochs=num_epochs, track_accuracy=False)