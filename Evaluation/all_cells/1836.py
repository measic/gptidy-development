score = model.evaluate(np.array(X_dev), y_dev_hot, batch_size=16)

print '\nAccuracy on test data', score[1]