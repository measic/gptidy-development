bottleneck_features = np.load('bottleneck_features/DogVGG16Data.npz')
train_VGG16 = bottleneck_features['train']
variable_def = bottleneck_features['valid']
test_VGG16 = bottleneck_features['test']