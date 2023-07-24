# Used X_test, y_test, and model.predict(X_test) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_20K, predictions_20K)
r2 = model_20K.score(X_test_20K, y_test_20K)


print(f"MSE: {MSE}, R2: {r2}")

# create lists of MSE and r2 values for each model

boston_models.append('20K')
boston_mse.append(MSE)
boston_r2.append(r2)
