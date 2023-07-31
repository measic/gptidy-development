for (_, _) in ('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf):
    _.fit(X_train, y_train)