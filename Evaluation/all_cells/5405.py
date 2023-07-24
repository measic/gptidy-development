# In order to use the full training set, merge training and validation set here and use cross validation
X_train = np.concatenate((X_train, X_valid), axis=0)
n_train = len(X_train)

print("Number of training examples =", n_train)
print("Number of testing examples =", n_test)