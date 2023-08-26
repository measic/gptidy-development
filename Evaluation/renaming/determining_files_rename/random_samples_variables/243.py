from sklearn.model_selection import StratifiedShuffleSplit, StratifiedKFold

def nparray_to_list(nparray):
    return [x for x in nparray]

def cv_split(X, y):
    variable_def = StratifiedShuffleSplit(n_splits=1, test_size=0.05)
    X_np = np.asarray(X)
    y_np = np.asarray(y)
    for train_index, valid_index in variable_def.split(X_np, y_np):
        X_train, X_valid = (nparray_to_list(X_np[train_index]), nparray_to_list(X_np[valid_index]))
        y_train, y_valid = (nparray_to_list(y_np[train_index]), nparray_to_list(y_np[valid_index]))
    train = (X_train, y_train)
    valid = (X_valid, y_valid)
    return (train, valid)