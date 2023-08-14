# Used X_test, y_test, and model.predict(X_test) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_Final, predictions_Final)
r2 = model_Final.score(X_test_Final, y_test_Final)


print(f"MSE: {MSE}, R2: {r2}")

# create lists of MSE and r2 values for each model

boston_models.append('Final')
boston_mse.append(MSE)
boston_r2.append(r2)
