for e in rnd_clf.estimators_:
    yt = e.predict(X_test)
    print(accuracy_score(y_test, yt))