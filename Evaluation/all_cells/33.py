# Define optimizer
optimizer = tf.train.GradientDescentOptimizer(1e-4)

# Initialize model 
model = two_layer_nn(output_size=1, loss_type='regression')

# Select here the number of epochs
num_epochs = 300

# Train the model with gradient descent
model.fit(X, y, optimizer, num_epochs=num_epochs, 
          track_accuracy=False)