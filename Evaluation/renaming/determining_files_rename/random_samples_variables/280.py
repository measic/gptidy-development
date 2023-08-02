variable_def = int(np.ceil(2 * len(y) / float(3)))
X_train = X[:variable_def, :]
y_train = y[:variable_def]
X_test = X[variable_def:, :]
y_test = y[variable_def:]
X_train = np.asarray(np.reshape(X_train, (X_train.shape[0], window_size, 1)))
X_test = np.asarray(np.reshape(X_test, (X_test.shape[0], window_size, 1)))