# Calculate accuracy.
accuracy = n_greater_50k/n_records

# Calculate F-score using the formula above for beta = 0.5. Done.
precision=n_greater_50k/(n_at_most_50k+n_greater_50k)
recall=n_greater_50k/(n_greater_50k+0)
beta=0.5
fscore = (1+beta**2)*precision*recall/((beta**2*precision)+recall)

# Print the results 
print "Naive Predictor: [Accuracy score: {:.4f}, F-score: {:.4f}]".format(accuracy, fscore)