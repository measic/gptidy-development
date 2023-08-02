def function_def(dataset, labels):
    permutation = np.random.permutation(labels.shape[0])
    shuffled_dataset = dataset[permutation, :, :]
    shuffled_labels = labels[permutation]
    return (shuffled_dataset, shuffled_labels)
train_dataset, train_labels = function_def(train_dataset, train_labels)
test_dataset, test_labels = function_def(test_dataset, test_labels)
valid_dataset, valid_labels = function_def(valid_dataset, valid_labels)