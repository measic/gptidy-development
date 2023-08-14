# Note: Use an alpha of .01 when creating the model for this activity
from sklearn.linear_model import ElasticNet

elasticnet_5K = ElasticNet(alpha=.01).fit(X_train_5K, y_train_5K)

predictions_5K = elasticnet_5K.predict(X_test_5K)

MSE = mean_squared_error(y_test_5K, predictions)
r2 = elasticnet_5K.score(X_test_5K, y_test_5K)


print(f"MSE: {MSE}, R2: {r2}")