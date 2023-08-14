# Features - remove the thing we're trying to predict!
features = data_full.drop('SalePrice', axis = 1)

# Create dummy variables - for each categorical data, make several boolean flags
features = pd.get_dummies(features)

# Make matrices to pass to scikit learn:
X_train = features[:train.shape[0]]
X_test = features[train.shape[0]:]
y = train['SalePrice']

# Verify that the number of features has been increased due to the dummy variables:
print('Number of features in original dataset, including categorical fields: ', train.shape[1], 
      '\nNumber of features, including dummy variables for categorical fields: ', X_train.shape[1])