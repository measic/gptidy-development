NUM_IN_CLASS = 800

def random_translate(img):
    rows, cols, ch = img.shape
    x = random.randint(-4, 4)
    y = random.randint(-4, 4)
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(img, M, (cols, rows))

def random_rotate(img):
    rows, cols, ch = img.shape
    degree = random.randint(-8, 8)
    M = cv.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)
    return cv.warpAffine(img, M, (cols, rows))

def random_zoom(img):
    x = random.randint(1, 5)
    y = random.randint(26, 31)
    pts1 = np.float32([[x, x], [y, x], [x, y], [y, y]])
    pts2 = np.float32([[0, 0], [31, 0], [0, 31], [31, 31]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    return cv.warpPerspective(img, M, (32, 32))

def random_transform_img(rand_img, transform_type_n=None):
    """
    transform_type_n:
        0: random_translate
        1: random_rotate
        2: random_zoom
    """
    transform_funcs = [random_translate, random_rotate, random_zoom]
    if transform_type_n:
        transform = transform_funcs[transform_type_n]
        return transform(rand_img)
    transform = random.choice(transform_funcs)
    return transform(rand_img)

def split_by_class(X_train, y_train):
    """
    Return data_by_classes, list of tuples, each tuple: (X_train_class_i, y_train_class_i)
    Note: X_train_class_i is a list, y_train_class_i is a number
    """
    variable_def = {}
    for i in range(len(y_train)):
        if y_train[i] not in variable_def:
            variable_def[y_train[i]] = [X_train[i]]
        else:
            variable_def[y_train[i]].append(X_train[i])
    data_by_classes = [(X_train_class_i, y_train_class_i) for y_train_class_i, X_train_class_i in variable_def.items()]
    return data_by_classes

def augment_by_class(training_data_tuple):
    """
    Augment the data by translating, rotating, zooming, until it has 1200 examples
    training_data_tuple: (X_train_class_i, y_train_class_i), 
    X_train_class_i is a list, y_train_class_i is a number
    """
    X_train_by_class = training_data_tuple[0]
    y_train_by_class = training_data_tuple[1]
    if len(X_train_by_class) >= NUM_IN_CLASS:
        return training_data_tuple
    while len(X_train_by_class) < NUM_IN_CLASS:
        rand_img = random.choice(X_train_by_class)
        new_img = random_transform_img(rand_img)
        X_train_by_class.append(new_img)
    return (X_train_by_class, y_train_by_class)

def merge_and_shuffle(augmented_data_by_classes):
    augmented_X_train = []
    augmented_y_train = []
    for augmented_tup in augmented_data_by_classes:
        for X_train_i in augmented_tup[0]:
            augmented_X_train.append(X_train_i)
            augmented_y_train.append(augmented_tup[1])
    X_train, y_train = shuffle(augmented_X_train, augmented_y_train)
    return (X_train, y_train)

def augment_data(X_train, y_train):
    """
    Main function to augment training data
    """
    data_by_classes = split_by_class(X_train, y_train)
    augmented_data_by_classes = []
    for tup in data_by_classes:
        augmented_tup = augment_by_class(tup)
        assert len(tup[0]) >= NUM_IN_CLASS, 'Class {0} still has {0} examples'.format(tup[1], len(tup[0]))
        augmented_data_by_classes.append(augmented_tup)
    return merge_and_shuffle(augmented_data_by_classes)
rand_img = random.choice(X_train)
transformed_img = random_translate(rand_img)
(plt.subplot(121), plt.imshow(rand_img), plt.title('Input'))
(plt.subplot(122), plt.imshow(transformed_img), plt.title('Output'))
plt.suptitle('Translation')
plt.show()
rand_img = random.choice(X_train)
transformed_img = random_rotate(rand_img)
(plt.subplot(121), plt.imshow(rand_img), plt.title('Input'))
(plt.subplot(122), plt.imshow(transformed_img), plt.title('Output'))
plt.suptitle('Rotation')
plt.show()
rand_img = random.choice(X_train)
transformed_img = random_zoom(rand_img)
(plt.subplot(121), plt.imshow(rand_img), plt.title('Input'))
(plt.subplot(122), plt.imshow(transformed_img), plt.title('Output'))
plt.suptitle('Zoom')
plt.show()
X_train_augmented, y_train_augmented = augment_data(X_train, y_train)