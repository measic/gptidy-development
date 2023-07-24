from sklearn.metrics import accuracy_score
y_predict = xgbc.predict(X_test)
rf_y_predict = rf.predict(X_test)
sgd_y_predict = sgd.predict(X_test)

print(" -- accuracy_score ---")
print(accuracy_score(y_test, y_predict))
print(accuracy_score(y_test, rf_y_predict))
print(accuracy_score(y_test, sgd_y_predict))