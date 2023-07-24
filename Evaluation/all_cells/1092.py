[test_loss, test_acc] = VGG16Seq.evaluate(arr_X_test, arr_y_test)
print("Evaluation result on Test Data : Loss = {}, accuracy = {}".format(test_loss, test_acc))