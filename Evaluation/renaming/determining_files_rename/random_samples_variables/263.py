y_scores = -probas_gmm
precision_gmm, variable_def, _ = metrics.precision_recall_curve(y_true, y_scores)
pr_auc_gmm = metrics.auc(variable_def, precision_gmm)
fpr_gmm, tpr_gmm, _ = metrics.roc_curve(y_true, y_scores)
auroc_gmm = metrics.roc_auc_score(y_true, y_scores)
print('AUROC: %.2f, PR AUC: %.2f' % (auroc_gmm, pr_auc_gmm))