# Create input features and targets dataset. Transfer data from numpy to tensors.
X = tf.constant(wine_data.data)
y = tf.constant(wine_data.target)