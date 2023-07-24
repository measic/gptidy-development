score3 = model3.evaluate(np.array(X_dev_dog), y_dev_hot, batch_size=16)

print '\nAccuracy on new dataset with only cat data is', score3[1]