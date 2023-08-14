lab = 'focus'
test_predictions = models[lab].predict(normed_test_data).flatten()
diff = test_labels[lab] - test_predictions
diff.idxmax(), diff.idxmin()