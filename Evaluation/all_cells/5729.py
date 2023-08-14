VALIDATION_PERCENTAGE = .2

X_train, y_train = shuffle(X_train, y_train)
X_train, X_valid, y_train , y_valid = train_test_split(X_train, y_train, test_size=VALIDATION_PERCENTAGE)
