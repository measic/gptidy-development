def reformat(dataset, labels):
  dataset = dataset.reshape(
    (-1, image_size, image_size, num_channels)).astype(np.float32)

  labels = (np.arange(n_classes) == labels[:,None]).astype(np.float32)
  return dataset, labels

X_train, y_train = reformat(X_train, y_train)
X_valid, y_valid = reformat(X_valid, y_valid)
X_test, y_test = reformat(X_test, y_test)

y_test_cls = np.argmax(y_test, axis=1)

print('Features set', X_train.shape, X_valid.shape, X_test.shape)
print('Labels set', y_train.shape, y_valid.shape, y_test.shape)