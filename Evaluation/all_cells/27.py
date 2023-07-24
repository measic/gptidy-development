# Apply Softmax on our predictions as the output of the model is unnormalized
# Select the predictions of our positive class (the class with less samples)
preds = tf.nn.softmax(model.predict(X))[:,1] 

# Compute the ROC-AUC score and get the TPR and FPR of each threshold
auc_score, fpr_list, tpr_list = roc_auc(y, preds, thresholds)