variable_def = np.load('bottleneck_features/DogVGG16Data.npz')
train_VGG16 = variable_def['train']
valid_VGG16 = variable_def['valid']
test_VGG16 = variable_def['test']