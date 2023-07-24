# This looks like it correpsonds to alpha = 30, so let's fit the model with that.
model_ridge = Ridge(alpha = 30)
model_ridge.fit(X_train, y)