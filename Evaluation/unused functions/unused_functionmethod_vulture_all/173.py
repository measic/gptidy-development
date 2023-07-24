def train_validate_test_split(df, y, train_percent=.6, validate_percent=.2, seed=0, shuffle=True):
    np.random.seed(seed)
    
    if shuffle:
        perm = np.random.permutation(df.index)
    else:
        perm = df.index

    train_end    = int(train_percent * len(df))
    validate_end = int(validate_percent * len(df)) + train_end

    
    x_train        = df.iloc[perm[:train_end]]
    x_validate     = df.iloc[perm[train_end:validate_end]]
    x_test         = df.iloc[perm[validate_end:]]
        
    y_train    = x_train[y]
    y_validate = x_validate[y]
    y_test     = x_test[y]
    
    x_train = x_train.drop(y, axis=1)
    x_validate = x_validate.drop(y, axis=1)
    x_test = x_test.drop(y, axis=1)

    return x_train, y_train, x_validate, y_validate, x_test, y_test


