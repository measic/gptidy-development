# Used X_test_5K, y_test_5K, and model.predict(X_test_5K) to calculate MSE and R2

from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(y_test_5K, predictions_5K)
r2 = model_5K.score(X_test_5K, y_test_5K)


print(f"MSE: {MSE}, R2: {r2}")

# create lists of MSE and r2 values for each model
boston_r2=[]
boston_mse=[]
boston_models = []

boston_models.append('5K')
boston_mse.append(MSE)
boston_r2.append(r2)

