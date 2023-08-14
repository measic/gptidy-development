### TODO: Obtain bottleneck features from another pre-trained CNN.

INCEPTION_BNECK = 'bottleneck_features/DogInceptionV3Data.npz'

bottleneck_features = np.load(INCEPTION_BNECK)
train_incp_bn = bottleneck_features['train']
valid_incp_bn = bottleneck_features['valid']
test_incp_bn  = bottleneck_features['test']