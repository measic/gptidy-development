pipe_knn = make_pipeline(MinMaxScaler(), SelectPercentile(), KNeighborsRegressor())
param_grid_knn = {'selectpercentile__percentile': range(10, 30, 5), 'kneighborsregressor__n_neighbors': range(1, 20), 'kneighborsregressor__weights': ['uniform', 'distance']}
knn_grid = GridSearchCV(pipe_knn, param_grid_knn)
knn_grid.fit(train_features, train_outcome)
knn_best_params = knn_grid.best_params_
knn_grid_score = knn_grid.score(test_features, test_outcome)
variable_def = mean_absolute_error(knn_grid.predict(test_features), test_outcome)
knn_evs = explained_variance_score(knn_grid.predict(test_features), test_outcome)