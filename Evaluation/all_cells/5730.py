IMAGES_PER_CLASS = 2500

X_train, y_train = get_augmented_images(X_train,y_train, img_ct_per_class = IMAGES_PER_CLASS)

print("New number of training examples =", X_train.shape[0])