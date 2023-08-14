#
#  Run classifier on each binary matrix, that has different
#  number of columns (genes).  Iterate through different
#  C values, using Logistic Regression L1 regularization 
#  to eliminate features.  Now run Logistic Regression, L2
#  regularization and keep track of precision, recall,
#  and confusion matrix.  Plot these metrics per feature
#  size and show the confusion matrix for the best performing
#  feature size.
#
def runClassifier(name, logit_c_param=.1, svm_c_param=.01):
    warnings.filterwarnings('ignore')
    data_object    = all_data[name]
    data          = data_object['data']
    labels        = data_object['labels']
    label_encoder = data_object['label_encoder']
    splits = splitData(data, labels)
    eliminateFeatures(splits['train_data'], splits['train_labels'],
                      splits['dev_data'], splits['dev_labels'], 
                      logit_c_param, svm_c_param, label_encoder)