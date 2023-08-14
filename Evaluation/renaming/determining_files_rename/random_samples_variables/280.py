train_test_split = int(np.ceil(2 * len(y) / float(3)))
X_train = X[:train_test_split, :]
y_train = y[:train_test_split]
variable_def = X[train_test_split:, :]
y_test = y[train_test_split:]
X_train = np.asarray(np.reshape(X_train, (X_train.shape[0], window_size, 1)))
variable_def = np.asarray(np.reshape(variable_def, (variable_def.shape[0], window_size, 1)))