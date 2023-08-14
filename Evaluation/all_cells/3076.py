# construct pipeline
pipe_dt = make_pipeline(
    MinMaxScaler(), # used to normalize data onto a similar scale
    SelectPercentile(), # used to filter out features that add noise
    DecisionTreeRegressor()
)

# create the parameter grid for hyperparameter tuning
param_grid_dt = {
    'selectpercentile__percentile':range(5, 30, 5), # what upper percentile of features to take
    'decisiontreeregressor__max_features':["auto", "sqrt", "log2", None], # the number of features to conside when splitting
    'decisiontreeregressor__max_depth':range(1, 10), # maximum depth of the decision tree
    'decisiontreeregressor__min_samples_leaf':range(1, 4) # minimum number of samples required to be at a leaf node
}

# perform grid search of pipeline
dt_grid = GridSearchCV(pipe_dt, param_grid_dt)

# use results to create model on training data
dt_grid.fit(train_features, train_outcome)

# find the best parameters from the grid search
dt_best_params = dt_grid.best_params_

# find the score of our model on the test data
dt_grid_score = dt_grid.score(test_features, test_outcome)

# find the mean absolute error of our model on the test data
dt_mae = mean_absolute_error(dt_grid.predict(test_features), test_outcome)

# find the explained variance score of our model on the test data
dt_evs = explained_variance_score(dt_grid.predict(test_features), test_outcome)