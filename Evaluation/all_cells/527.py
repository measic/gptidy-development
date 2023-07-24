diag_classifier = LinearRegression()
# Train Diagnostic Classifier
diag_classifier.fit(train_hiddens, train_hyps)