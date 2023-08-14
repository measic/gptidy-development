tuned_parameters = [{'kernel': ['rbf'], 'nu': [0.0001, 0.001, 0.01, 0.1, 0.5]}, {'kernel': ['poly'], 'degree': np.arange(1, 4), 'nu': [0.0001, 0.001, 0.01, 0.1, 0.5], 'max_iter': [10000]}]
variable_def = ParameterSearch(svm.OneClassSVM, tuned_parameters, act_train_svm, act_train_all, pred_f_tr.flatten(), scorer_roc_probas_svm, n_iter=5, verbosity=11, n_jobs=-1, subsample_train=0.01, subsample_test=0.001)
variable_def.fit()