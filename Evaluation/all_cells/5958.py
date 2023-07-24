from sklearn.ensemble import RandomForestClassifier

plot_validation_curve(RandomForestClassifier(n_estimators=300),X_dev_np, y_dev_np,
                      "max_features", range(1,201,10),
                      "Curvas para Random Forest con 300 arboles", "max_features")

plot_validation_curve(RandomForestClassifier(n_estimators=200),X_dev_np, y_dev_np,
                      "max_features", range(1,201,10),
                      "Curvas para Random Forest con 200 arboles", "max_features")

plot_validation_curve(RandomForestClassifier(n_estimators=30),X_dev_np, y_dev_np,
                      "max_features", range(1,201,10),
                      "Curvas para Random Forest con 30 arboles", "max_features")