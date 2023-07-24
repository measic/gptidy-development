## Show a detailed summary of the cross validation metrics
## This gives you an idea of the variance between the folds
cv_summary = cv_gbm.cross_validation_metrics_summary().as_data_frame()
#print(cv_summary) ## Full summary of all metrics
#print(cv_summary.iloc[4]) ## get the row with just the AUCs

## Get the cross-validated AUC by scoring the combined holdout predictions.
## (Instead of taking the average of the metrics across the folds)
perf_cv = cv_gbm.model_performance(xval=True)
print perf_cv.auc()