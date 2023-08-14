# Used X_test, y_test, and model.predict(X_test) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_40K, predictions_40K)
r2 = model_40K.score(X_test_40K, y_test_40K)


print(f"MSE: {MSE}, R2: {r2}")

# create lists of MSE and r2 values for each model

boston_models.append('40K')
boston_mse.append(MSE)
boston_r2.append(r2)