def getBestParams(train_data, train_labels):
    #mini_train_data, mini_test_data, mini_train_labels, mini_test_labels = train_test_split(train_data, train_labels,
    #                                    stratify=train_labels, 
    #                                    test_size=0.55)
    
    #
    # Logistic Regression
    #
    lr = LogisticRegression(penalty='l2', multi_class = 'ovr', solver='liblinear', max_iter=150)
    params = {'C': [0.1, 0.25,  0.5,]}
    logit = GridSearchCV(lr, params, cv=5,
                         scoring='accuracy', return_train_score=True)

    # Fit  training data
    logit.fit(train_data, train_labels)  
    # Show the best C parameter to use and the expected accuracy
    print('\nLogistic Regression Classifier, L2 regularization')
    print(' Best param:', logit.best_params_)
    print(' Accuracy:  ', np.round(logit.best_score_, 4) )
    
    return logit.best_params_