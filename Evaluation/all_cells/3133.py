for train_index, test_index in split.split(X, y):
    X_train, X_test = X[train_index], y[test_index]
    y_train, y_test = y[train_index], y[test_index]