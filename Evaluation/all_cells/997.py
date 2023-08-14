X_model = X[model_features].copy()
X_train, X_test, y_train, y_test = train_test_split(X_model, y, test_size=0.2, random_state= 5)
X_train = X_train.copy()
X_test = X_test.copy()
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

scaler.fit(X_train[numeric_model_features])
X_train[numeric_model_features] = scaler.transform(X_train[numeric_model_features])
X_test[numeric_model_features] = scaler.transform(X_test[numeric_model_features])

logreg.fit(X_train,y_train)

y_pred = logreg.predict(X_test)
# save model stats
prediction_probabilities = logreg.predict_proba(X_test)

cross_val_scores = cross_val_score(logreg, X,y, cv=10, scoring='accuracy')
cross_validation_average = cross_val_scores.mean()

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("Log loss= ",log_loss(y_test, prediction_probabilities))

utils.display_confusion_matrix(y_test, y_pred)