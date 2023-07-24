def eliminateFeatures(train_data, train_labels, dev_data, dev_labels, 
                      logit_C_param, svm_C_param, label_encoder):

    params = {'C':  [1000, 100, 10, 1, .5, .3, .1, .05]}


    # Now perform logistic regression on this training set with reduced features
    # as well as the orginal non-reduced training set.  Run over different
    # C values to plot differences in accuracy
    precision_l1        = []
    recall_l1           = []
    
    accuracy            = []
    precision           = []
    recall              = []
    precision_by_label  = []
    recall_by_label     = []
    
    svm_accuracy            = []
    svm_precision           = []
    svm_recall              = []
    svm_precision_by_label  = []
    svm_recall_by_label     = []

    feature_size        = []
    confusion           = []


    for c_param in reversed(params['C']):
        # Keep this random seed here to make comparison easier.
        np.random.seed(0)

        #
        # Perform Logistic Regression on different C values
        # using L1 regularization
        #
        l1_info = runLogitL1(train_data, train_labels, dev_data, dev_labels, c_param)    
        non_zero_genes = l1_info['non_zero_genes']
        feature_size.append(str(len(non_zero_genes)) + ' (L1 C=' + str(c_param) + ")")
        precision_l1.append(l1_info['scores'][0])
        recall_l1.append(l1_info['scores'][1])


        #
        # Reduce feature size, only keeping features with non-zero weights 
        # found using l1 regularization
        #
        min_train_data = train_data[non_zero_genes]
        min_dev_data   = dev_data[non_zero_genes]


        # Run logistic regression with L2 regularization on reduced
        # feature set
        lr = LogisticRegression(penalty='l2', tol=.01, max_iter=150, 
                                C=logit_C_param, solver="liblinear", multi_class="ovr")
        lr.fit(min_train_data, train_labels) 
        predict = lr.predict(min_dev_data)

        # Get precision, recall, f1 scores
        the_accuracy = accuracy_score(dev_labels, predict)
        scores = precision_recall_fscore_support(dev_labels, predict, average='weighted')
        scores_by_label = precision_recall_fscore_support(dev_labels, predict, average=None)

        # Get confusion matrix
        confusion_mx = confusion_matrix(dev_labels, predict)

        accuracy.append(the_accuracy)
        precision.append(scores[0])
        recall.append(scores[1])
        precision_by_label.append(scores_by_label[0])
        recall_by_label.append(scores_by_label[1])
        confusion.append(confusion_mx)
        
        #
        # Run Linear SVM
        #
        svm = LinearSVC(penalty='l2', C=svm_C_param)

        svm.fit(min_train_data, train_labels,) 
        predict = svm.predict(min_dev_data)

        # Get precision, recall, f1 scores
        svm_accuracy_score = accuracy_score(dev_labels, predict)
        svm_scores = precision_recall_fscore_support(dev_labels, predict, average='weighted')
        svm_scores_by_label = precision_recall_fscore_support(dev_labels, predict, average=None)

        svm_accuracy.append(svm_accuracy_score)
        svm_precision.append(svm_scores[0])
        svm_recall.append(svm_scores[1])
        svm_precision_by_label.append(svm_scores_by_label[0])
        svm_recall_by_label.append(svm_scores_by_label[1])
    
    # print best precision and recall 
    best_idx = np.argmax(precision)
    print("\nBest precision", feature_size[best_idx])
    print("  precision:", np.round(precision[best_idx], 4))  
    print("  recall:   ", np.round(recall[best_idx], 4))  

    best_idx = np.argmax(recall)
    print("\nBest recall", feature_size[best_idx])
    print("  precision:", np.round(precision[best_idx], 4))  
    print("  recall:   ", np.round(recall[best_idx], 4))  
    

    plotMetrics(precision_l1, recall_l1, 
                accuracy, precision, recall, 
                precision_by_label, recall_by_label,
                svm_accuracy, svm_precision, svm_recall, 
                svm_precision_by_label, svm_recall_by_label,
                confusion, feature_size, label_encoder)
