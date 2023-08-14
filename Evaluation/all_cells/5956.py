parametrosRF = {
    "max_features": ["sqrt", "log2", None] + [1, 20, 50, 100, 150, 200],
    "max_depth": [3, 6, 12],
    "min_samples_split": [2, 6, 12],
    "n_estimators": [10, 50, 120, 200]
}

(tiempo_random_forest, grid_random_forest) = correr_y_mostrar(
    RandomForestClassifier(),
    parametrosRF,
    5,
    5
)

randomForest = grid_random_forest.best_estimator_
plot_learning_curve(randomForest, "Learning Curve Random Forest Mejor segun GridSearch", X_dev_np, y_dev_np, cv=5)