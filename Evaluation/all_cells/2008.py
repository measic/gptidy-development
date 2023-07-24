# Used X_test, y_test, and model.predict(X_test) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_F40K, predictions_F40K)
r2 = model_F40K.score(X_test_F40K, y_test_F40K)


print(f"MSE: {MSE}, R2: {r2}")

# create lists of MSE and r2 values for each model

# boston_models.append('F40K')
# boston_mse.append(MSE)
# boston_r2.append(r2)

# boston_residuals_df=pd.DataFrame({
#     'boston_models':boston_models,
#     'boston_mse':boston_mse,
#     'boston_r2':boston_r2
# })
boston_residuals_df