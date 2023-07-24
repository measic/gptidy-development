## Get the AUC on the validation set
perf = gbm.model_performance(valid)
print perf.auc()