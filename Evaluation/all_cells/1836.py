print("Classification Report: Dogs")
print(classification_report(y_dog_dev, test_dog_lr.predict(X_dog_dev), target_names=class_names))
print '\n'

print("Classification Report: Cats")
print(classification_report(y_cat_dev, test_cat_lr.predict(X_cat_dev), target_names=class_names))
print '\n'