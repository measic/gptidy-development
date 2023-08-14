#train model on PCA, 2 components
model_2 = RandomForestClassifier().fit(X_train_2d, y_train)
model_2.score(X_test_2d, y_test)