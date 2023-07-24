score2 = model2.evaluate(np.array(X_dev_feature), y_dev_hot, batch_size=16)

print '\nAccuracy on new dataset with no unknown columns is', score2[1]