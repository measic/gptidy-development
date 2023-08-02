# Train the model
AdaModel = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(),
                             n_estimators=100, learning_rate=0.05)
AdaModel = AdaModel.fit(X_train, y_train)
y_pred = AdaModel.predict(X_train)
