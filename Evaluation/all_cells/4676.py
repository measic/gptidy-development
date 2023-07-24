### TODO: Calculate classification accuracy on the test dataset.

#### Test the network

# get index of predicted dog breed for each img in test set
predictions = [np.argmax(inception_bneck.predict(np.expand_dims(feature, axis=0)))
              for feature in test_incp_bn]

# test accuracy
test_accuracy = 100. * np.sum(np.array(predictions) == np.argmax(test_targets, axis=1)) / len(predictions)

print('Test accuracy: {:.4f}%'.format(test_accuracy))