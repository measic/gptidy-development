from sklearn.model_selection import StratifiedShuffleSplit, StratifiedKFold

def function_def(nparray):
    return [x for x in nparray]

def cv_split(X, y):
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.05)
    X_np = np.asarray(X)
    y_np = np.asarray(y)
    for train_index, valid_index in sss.split(X_np, y_np):
        X_train, X_valid = (function_def(X_np[train_index]), function_def(X_np[valid_index]))
        y_train, y_valid = (function_def(y_np[train_index]), function_def(y_np[valid_index]))
    train = (X_train, y_train)
    valid = (X_valid, y_valid)
    return (train, valid)