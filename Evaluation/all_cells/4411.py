bag_clf = BaggingClassifier( 
    DecisionTreeClassifier(), 
    n_estimators=500,
    bootstrap=True, 
    random_state=42,
    n_jobs=-1, 
    oob_score=True)
bag_clf.fit(X_train, y_train) 
bag_clf.oob_score_