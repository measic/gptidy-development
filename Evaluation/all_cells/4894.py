# Display the predictions
for i, pred in zip(log_samples.index, sample_preds):
    print "Sample point", i, "predicted to be in Cluster", pred