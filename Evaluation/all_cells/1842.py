score4 = model4.evaluate(np.array(X_dev_cat), y_dev_hot, batch_size=16)

print '\nAccuracy on new dataset with only dog data is', score4[1]