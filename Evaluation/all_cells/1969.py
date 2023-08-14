# Used X_test, y_test, and model.predict(X_test) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_nobib, predictions)
r2 = model_nobib.score(X_test_nobib, y_test_nobib)


print(f"MSE: {MSE}, R2: {r2}")

# Model built without Bib numbers has a smaller R2 value, so Bib numbers was helping model predictions

# create lists of MSE and r2 values for each model

# boston_models.append('nobib')
# boston_mse.append(MSE)
# boston_r2.append(r2)
