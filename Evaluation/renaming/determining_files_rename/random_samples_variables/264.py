variable_def = (-get_acc_net_msr(y_pred_te)).flatten()
y_true = pred_f_te.flatten()
precision_msr, recall_msr, _ = metrics.precision_recall_curve(y_true, variable_def)
pr_auc_msr = metrics.average_precision_score(y_true, variable_def)
auroc_msr = metrics.roc_auc_score(y_true, variable_def)
fpr_msr, tpr_msr, _ = metrics.roc_curve(y_true, variable_def)
variable_def = (-get_acc_net_max_margin(y_pred_te)).flatten()
precision_margin, recall_margin, _ = metrics.precision_recall_curve(y_true, variable_def)
pr_auc_margin = metrics.average_precision_score(y_true, variable_def)
auroc_margin = metrics.roc_auc_score(y_true, variable_def)
fpr_margin, tpr_margin, _ = metrics.roc_curve(y_true, variable_def)
variable_def = (-get_acc_net_entropy(y_pred_te)).flatten()
precision_entropy, recall_entropy, _ = metrics.precision_recall_curve(y_true, variable_def)
pr_auc_entropy = metrics.average_precision_score(y_true, variable_def)
auroc_entropy = metrics.roc_auc_score(y_true, variable_def)
fpr_entropy, tpr_entropy, _ = metrics.roc_curve(y_true, variable_def)