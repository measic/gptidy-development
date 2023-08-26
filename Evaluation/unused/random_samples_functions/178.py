def plotMetrics(precision_l1, recall_l1, 
                accuracy, precision, recall, 
                precision_by_label, recall_by_label, 
                svm_accuracy, svm_precision, svm_recall, 
                svm_precision_by_label, svm_recall_by_label, 
                confusion, feature_size, label_encoder):
    labels = [ '\n'.join(wrap(l, 8)) for l in feature_size ]       
    
    plt.rcParams["figure.figsize"] = (20,6)

    plt.plot(labels, precision, color='olivedrab', 
             linewidth=3, label='Precision (Logistic regression) ', marker='o' )
    plt.plot(labels, recall, color='olivedrab', linestyle='dashed',
             linewidth=3, label='Recall (Logistic regression)', marker='o' )
    #plt.plot(labels, accuracy, color='darkolivegreen', linestyle=':',
    #         linewidth=3, label='Accuracy (Logistic regression)', marker='v' )

    plt.plot(labels, svm_precision, color='slateblue', 
             linewidth=3, label='Precision (SVM)', marker='o' )
    plt.plot(labels, svm_recall, color='slateblue', linestyle='dashed',
             linewidth=3, label='Recall (SVM)', marker='o' )
    #plt.plot(labels, svm_accuracy, color='darkslateblue', linestyle=':',
    #         linewidth=3, label='Accuracy (SVM)', marker='v' )

    #plt.plot(labels, precision_l1, color='gray',alpha=.4,
    #         linewidth=3, label='L1 precision at different C values', marker='o' )
    #plt.plot(labels, recall_l1, color='gray', linestyle='dashed',alpha=.6,
    #         linewidth=3, label='L1 at different C values', marker='o' )
    
    
    plt.yticks(np.arange(.42, .65, .01))
    plt.ylabel('Precision, Recall', fontsize=20)
    plt.xlabel('Feature size with L1 regularization at different C parameters', fontsize=20, labelpad=20)
    plt.legend()
    plt.grid()
    plt.show()
    
    # find optimal f1
    best_idx = np.argmax(precision)
    
    # Show precision and recall across different labels
    showPrecisionRecallPairByLabel(precision_by_label[best_idx], recall_by_label[best_idx], label_encoder,
                                  'Logistic Regression', ['olivedrab', 'darkolivegreen'])
    showPrecisionRecallPairByLabel(svm_precision_by_label[best_idx], svm_recall_by_label[best_idx], label_encoder,
                                  'SVM', ['slateblue', 'darkslateblue'])
    
    
    # Get the confusion matrix for the optimal precision
    # Show the labels that have the highest error rate
    conf_mx = confusion[best_idx]
    showTopConfused(conf_mx, label_encoder)
    
