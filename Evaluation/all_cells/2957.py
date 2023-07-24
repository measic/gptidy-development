#
#  Find best C param for Logistic Regression L2
#
data   = all_data['best_fit_1000']['data']
labels = all_data['best_fit_1000']['labels']
splits = splitData(data, labels)
logit_best_params = getBestParams(splits['train_data'], splits['train_labels'])

#
#  Find best C param for Linear SVM
#
svm_best_params = getBestParamsSVM(splits['train_data'], splits['train_labels'])


print("\n\n")


#
#  Find best C param for Logistic Regression L2
#
data   = all_data['best_fit_8000']['data']
labels = all_data['best_fit_8000']['labels']
splits = splitData(data, labels)
logit_best_params = getBestParams(splits['train_data'], splits['train_labels'])

#
#  Find best C param for Linear SVM
#
svm_best_params = getBestParamsSVM(splits['train_data'], splits['train_labels'])