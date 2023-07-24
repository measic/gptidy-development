
def get_augmented_images(X,y,img_ct_per_class = 2500):
    '''
    This function creates the necessary number of images so that each class
    has the same number of images (img_ct_per_class)
    '''
    aug_images = []
    aug_labels = []
    for cl in range(0,n_classes):
        y_class = np.where(y == cl)
        idx_class = y_class[0]
        X_class = X[idx_class]
        tmp_x,tmp_y = get_augmented_images_by_class(X=X_class, cl=cl, final_length = img_ct_per_class)

        aug_images.extend(tmp_x)
        aug_labels.extend(tmp_y)
        
    X_aug = np.stack(aug_images, axis = 0)
    Y_aug = np.stack(aug_labels, axis = 0)
    
    return (X_aug,Y_aug)
    

def get_augmented_images_by_class(X,cl,final_length):
    tmp_x = []
    for im in X:
        tmp_x.append(im)
    original_length = X.shape[0]
    tmp_y = [cl] * original_length
    
    add_length = final_length - original_length
    for _ in range(add_length):
        img_to_augment = X[np.random.randint(0,original_length)]
        new_img = transform_image(img_to_augment, 20, 10, 5)
        tmp_x.append(new_img)
    tmp_y.extend([cl] * add_length)
    return tmp_x, tmp_y
        