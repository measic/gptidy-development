# construct pipeline
pipe_knn = make_pipeline(
    MinMaxScaler(), # used to normalize data onto a similar scale
    SelectPercentile(), # used to filter out features that add noise
    KNeighborsRegressor()
)

# create the parameter grid for hyperparameter tuning
param_grid_knn = {
    'selectpercentile__percentile':range(10, 30, 5), # what upper percentile of features to take
    'kneighborsregressor__n_neighbors':range(1, 20), # the number of neighbors to take
    'kneighborsregressor__weights':["uniform", "distance"] # how to weight the connections between neighbors
}

# perform grid search of pipeline
knn_grid = GridSearchCV(pipe_knn, param_grid_knn)

# use results to create model on training data
knn_grid.fit(train_features, train_outcome)

# find the best parameters from the grid search
knn_best_params = knn_grid.best_params_

# find the score of our model on the test data
knn_grid_score = knn_grid.score(test_features, test_outcome)

# find the mean absolute error of our model on the test data
knn_mae = mean_absolute_error(knn_grid.predict(test_features), test_outcome)

# find the explained variance score of our model on the test data
knn_evs = explained_variance_score(knn_grid.predict(test_features), test_outcome)