def get_class_image(X_train, y_train, class_label):
    for i in range(len(y_train)):
        if y_train[i] == class_label:
            return X_train[i]
    return False

def show_class_images():
    fig, axes = plt.subplots(6, 8, figsize=(15, 10))
    fig.subplots_adjust(hspace = .8, wspace=.05)
    axes = axes.ravel()

    for i in range(43):
        class_image = get_class_image(X_train, y_train, i)
        axes[i].imshow(class_image, cmap="gray")
        axes[i].set_title(str(i))

show_class_images()