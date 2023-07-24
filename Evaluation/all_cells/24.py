# Define optimizer
optimizer = tf.train.GradientDescentOptimizer(5e-1)

# Initialize model 
model = two_layer_nn(output_size=2)

# Select here the number of epochs
num_epochs = 5

# Train the model with gradient descent
model.fit(X, y, optimizer, num_epochs=num_epochs)