# Imputing Functions

def UNIQ(X, value=-1):
    """Replace missing Values with unique value"""
    
    X.fillna(value=value, inplace=True)    
    return X

def MEAN(X):
    """Replace missing values with the mean of the others"""
    
    mean = np.mean(X)
    X.fillna(value=mean, inplace=True)
    return X

def MED(X):
    """Replace missing values with median of data"""
    
    median = np.nanmedian(X)
    X.fillna(value=median, inplace=True)
    return X

def CONST(X, value=0):
    """Replace missing values with a constant."""
    
    X.fillna(value=int(value), inplace=True)
    return X

def MODE(X):
    """Replace missing values with the mode."""
    
    mode = stats.mode(X)[0][0]
    X.fillna(value=mode, inplace=True)
    return X

def DEL(df_cv, df_all, col_name, feature_names):
    df_cv = df_cv.drop(col_name, axis=1)
    df_all = df_all.drop(col_name, axis=1)
    feature_names.remove(col_name)
    
    return df_cv, df_all, feature_names