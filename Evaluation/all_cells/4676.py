### TODO: Write a function that takes a path to an image as input
### and returns the dog breed that is predicted by the model.

# checkpoint file
inception_ckpoint_file = 'saved_models/inceptionv3_bneck.weights.hdf5'

# load weights
inception_bneck.load_weights(inception_ckpoint_file)