ridge_preds = np.expm1(model_ridge.predict(X_test))
lasso_preds = np.expm1(model_lasso.predict(X_test))
elastic_preds = np.expm1(model_elastic.predict(X_test))