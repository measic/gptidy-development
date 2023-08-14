from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_predict,labels=["B-LOC","B-MISC","B-ORG","B-PER","I-LOC","I-MISC","I-ORG","I-PER","O"]))

# cm = confusion_matrix(y_test, y_predict)
# pl.matshow(cm)
# pl.title('Confusion matrix of the classifier')
# pl.colorbar()
# pl.show()