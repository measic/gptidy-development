from sklearn.ensemble import GradientBoostingClassifier

parametrosGB = {
    "loss": ['deviance', 'exponential'],
    "criterion": ['mse', 'friedman_mse'],
    "learning_rate": np.linspace(0.1,1,100),
    "max_features": ["sqrt", "log2", None] + [1, 20, 50, 100, 150, 200],
    "max_depth": [3, 6, 12],
    "min_samples_split": [2, 6, 12],
    "subsample": [0.3, 0.5, 0.8, 0.9, 1.0],
    "n_estimators": range(1,200)
}
(tiempo_gb, random_grid_gb) = correr_randomized_y_mostrar(
    GradientBoostingClassifier(), 
    parametrosGB, 
    5, 
    5, 
    50
)

plot_learning_curve(
    random_grid_gb.best_estimator_, 
    "Curva de aprendizaje para gradient boosting",
    X_dev_np, 
    y_dev_np, 
    cv=5
)