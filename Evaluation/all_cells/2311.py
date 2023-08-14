# Split the training data into separate train and test sets
(X_train, X_test, y_train, y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

# Convert the labels (letters) into one-hot encodings that Keras can work with
le = LabelEncoder().fit(np.stack(list(y_train) + list(y_test)))
y_train = le.transform(y_train)
y_test = le.transform(y_test)