def getBestParamsSVM(train_data, train_labels):
    #mini_train_data, mini_test_data, mini_train_labels, mini_test_labels = train_test_split(train_data, train_labels,
    #                                    stratify=train_labels, 
    #                                    test_size=0.55)
    
    #
    # SVM
    #
    classifier = LinearSVC(penalty='l2')

    params = {'C': [0.01, 0.1, 0.5]}
    svm = GridSearchCV(classifier, params, cv=4, 
                       scoring='accuracy', return_train_score=True)

    # Fit  training data
    svm.fit(train_data, train_labels)  
    # Show the best C parameter to use and the expected accuracy
    print('\nSVM Classifier')
    print(' Best param:', svm.best_params_)
    print(' Accuracy:  ', np.round(svm.best_score_, 4) )
    
    return svm.best_params_