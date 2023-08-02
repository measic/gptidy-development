from sklearn.model_selection import train_test_split
X_train, X_test, y_train, variable_def = train_test_split(features_final, income, test_size=0.2, random_state=0)
print('Training set has {} samples.'.format(X_train.shape[0]))
print('Testing set has {} samples.'.format(X_test.shape[0]))