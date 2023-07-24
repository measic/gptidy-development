# Predict

result_1 = []
for p in [log_clf_s, rnd_clf_s, svm_clf_s]:
    result_1.append(p.predict(X_test))

y_pred_s = rnd_clf_2.predict(np.column_stack(tuple(result_1)))
accuracy_score(y_test, y_pred_s)