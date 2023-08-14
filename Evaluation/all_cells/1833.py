def plot_confusion_matrix(cm, classes, normalize = False, title = 'Confusion Matrix', cmap = plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

class_names = ['Return_to_owner', 'Euthanasia', 'Adoption', 'Transfer', 'Died']
cnf_dog_matrix = confusion_matrix(y_dog_dev, test_dog_lr.predict(X_dog_dev), labels = class_names)
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_dog_matrix, classes=class_names, normalize = True,
                      title='Confusion matrix for Dogs, with normalization')

cnf_cat_matrix = confusion_matrix(y_cat_dev, test_cat_lr.predict(X_cat_dev), labels = class_names)
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(cnf_cat_matrix, classes=class_names, normalize = True,
                      title='Confusion matrix for Cats, with normalization')
plt.show()