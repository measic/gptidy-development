%%time
y_test_pred = AdaModel.predict(X_test)
print(accuracy_score(y_test, y_test_pred))