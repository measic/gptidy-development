variable_def = -probas_gmm
precision_gmm, recall_gmm, _ = metrics.precision_recall_curve(y_true, variable_def)
pr_auc_gmm = metrics.auc(recall_gmm, precision_gmm)
fpr_gmm, tpr_gmm, _ = metrics.roc_curve(y_true, variable_def)
auroc_gmm = metrics.roc_auc_score(y_true, variable_def)
print('AUROC: %.2f, PR AUC: %.2f' % (auroc_gmm, pr_auc_gmm))