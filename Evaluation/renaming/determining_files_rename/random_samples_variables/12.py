from sklearn.model_selection import StratifiedShuffleSplit, StratifiedKFold

def nparray_to_list(nparray):
    return [x for x in nparray]

def cv_split(X, y):
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.05)
    variable_def = np.asarray(X)
    y_np = np.asarray(y)
    for train_index, valid_index in sss.split(variable_def, y_np):
        X_train, X_valid = (nparray_to_list(variable_def[train_index]), nparray_to_list(variable_def[valid_index]))
        y_train, y_valid = (nparray_to_list(y_np[train_index]), nparray_to_list(y_np[valid_index]))
    train = (X_train, y_train)
    valid = (X_valid, y_valid)
    return (train, valid)