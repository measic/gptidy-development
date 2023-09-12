class two_layer_nn(tf.keras.Model):

    def __init__(self, output_size=2, loss_type='cross-entropy'):
        super(two_layer_nn, self).__init__()
        " Define here the layers used during the forward-pass \n            of the neural network.     \n            Args:\n                output_size: int (default=2). \n                loss_type: string, 'cross-entropy' or 'regression' (default='cross-entropy')\n        "
        self.dense_1 = tf.layers.Dense(20, activation=tf.nn.relu)
        self.dense_2 = tf.layers.Dense(10, activation=tf.nn.relu)
        self.dense_out = tf.layers.Dense(output_size, activation=None)
        self.loss_type = loss_type

    def predict(self, input_data):
        """ Runs a forward-pass through the network.     
            Args:
                input_data: 2D tensor of shape (n_samples, n_features).   
            Returns:
                logits: unnormalized predictions.
        """
        layer_1 = self.dense_1(input_data)
        layer_2 = self.dense_2(layer_1)
        logits = self.dense_out(layer_2)
        return logits

    def function_def(self, input_data, target):
        """ Defines the loss function used during 
            training.         
        """
        preds = self.predict(input_data)
        if self.loss_type == 'cross-entropy':
            loss = tf.losses.sparse_softmax_cross_entropy(labels=target, logits=preds)
        else:
            loss = tf.losses.mean_squared_error(target, preds)
        return loss

    def grads_fn(self, input_data, target):
        """ Dynamically computes the gradients of the loss value
            with respect to the parameters of the model, in each
            forward pass.
        """
        with tfe.GradientTape() as tape:
            loss = self.function_def(input_data, target)
        return tape.gradient(loss, self.variables)

    def fit(self, input_data, target, optimizer, num_epochs=500, verbose=50, track_accuracy=True):
        """ Function to train the model, using the selected optimizer and
            for the desired number of epochs. It also stores the accuracy
            of the model after each epoch.
        """
        if track_accuracy:
            self.hist_accuracy = []
            accuracy = tfe.metrics.Accuracy()
        for i in range(num_epochs):
            grads = self.grads_fn(input_data, target)
            optimizer.apply_gradients(zip(grads, self.variables))
            if track_accuracy:
                logits = self.predict(X)
                preds = tf.argmax(logits, axis=1)
                accuracy(preds, target)
                self.hist_accuracy.append(accuracy.result())
                accuracy.init_variables()