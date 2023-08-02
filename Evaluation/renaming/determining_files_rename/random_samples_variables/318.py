TP = np.sum(income)
FP = income.count() - TP
TN = 0
FN = 0
accuracy = 1.0 * (TP + TN) / (TP + TN + FP + FN)
variable_def = 1.0 * TP / (TP + FN)
precision = 1.0 * TP / (TP + FP)
fscore = (1.0 + 0.5 * 0.5) * (precision * variable_def) / (0.5 * 0.5 * precision + variable_def)
print('Naive Predictor: [Accuracy score: {}, F-score: {}]'.format(accuracy, fscore))