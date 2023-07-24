missed_predictions = get_missed_predictions(
    tourney_comp_ratings, model_features, numeric_model_features,
    prediction_probabilities, X_test, y_test, y_pred
)