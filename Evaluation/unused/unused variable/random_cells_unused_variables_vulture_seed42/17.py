for (name, prd) in ('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf):
    prd.fit(X_train, y_train)