y_scores = -probas_svm
precision_svm, recall_svm, _ = metrics.precision_recall_curve(y_true, y_scores)
pr_auc_svm = metrics.auc(recall_svm, precision_svm)
fpr_svm, tpr_svm, _ = metrics.roc_curve(y_true, y_scores)
variable_def = metrics.roc_auc_score(y_true, y_scores)