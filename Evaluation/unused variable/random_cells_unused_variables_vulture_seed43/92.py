hyperparameter = ex.literal(v = 5, name="hyperparameters")
#Define the model training and evaluation action and final artifacts
do_test = ex.action(train_test, [X_train, X_test, y_train, y_test, hyperparameter])
report = ex.artifact('report.csv', 'report', do_test)