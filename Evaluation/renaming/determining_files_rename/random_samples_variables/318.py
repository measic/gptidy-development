TP = np.sum(income)
FP = income.count() - TP
variable_def = 0
FN = 0
accuracy = 1.0 * (TP + variable_def) / (TP + variable_def + FP + FN)
recall = 1.0 * TP / (TP + FN)
precision = 1.0 * TP / (TP + FP)
fscore = (1.0 + 0.5 * 0.5) * (precision * recall) / (0.5 * 0.5 * precision + recall)
print('Naive Predictor: [Accuracy score: {}, F-score: {}]'.format(accuracy, fscore))