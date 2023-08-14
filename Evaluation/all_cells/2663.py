# Counting the ones as this is the naive case. Note that 'income' is the 'income_raw' data 
# encoded to numerical values done in the data preprocessing step.
TP = np.sum(income)

# Specific to the naive case
FP = income.count() - TP

TN = 0 # No predicted negatives in the naive case
FN = 0 # No predicted negatives in the naive case

# Calculate accuracy, precision and recall
accuracy = 1.0 * (TP+TN) / (TP+TN+FP+FN)
recall = 1.0 * TP / (TP+FN)
precision = 1.0 * TP / (TP+FP)

# Calculate F-score using the formula above for beta = 0.5 and correct values for precision and recall.
fscore = ((1.0 + 0.5 * 0.5) * (precision * recall)) / ((0.5 * 0.5 * precision) + recall)

# Print the results 
print("Naive Predictor: [Accuracy score: {}, F-score: {}]".format(accuracy, fscore))