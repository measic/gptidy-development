# Encoding Functions

def MAP(X):
    """Map all values to integer numbers."""
    """NaN values are treated as a unique value."""
    
    # create an encoding for categorical vars
    unique_elems = set(X)
    mapping = {label:idx for idx, label in enumerate(unique_elems)}
    return X.map(mapping).astype(int)

def LOO(X):
    """Perform Leave One Out counting for the features."""
    
    # map features to ordinal values first
    X = MAP(X)
    
    # perform counts
    mapping = {idx:(count-1) for idx, count in enumerate(np.bincount(X))}
    return X.map(mapping).astype(int)
    

def OHE(df_cv, df_all, col_name, feature_names, feature_threshold=0.02):
    """Map categorical values to a one hot encoding scheme."""
    
    X_cv = MAP(df_cv[col_name])
    X_all = MAP(df_all[col_name])
    
    X_cv = X_cv.values.reshape(-1, 1)
    X_all = X_all.values.reshape(-1, 1)
    OHE = OneHotEncoder(sparse=False).fit(X_all)
    X_cv_ohe = OHE.transform(X_cv)
    X_all_ohe = OHE.transform(X_all)
    
    low_freq_features = []
    for i in range(X_all_ohe.shape[1]):
        new_feature = col_name + str(i)
        
        # determine the frequency of the categorical data value
        freq = np.sum(X_all_ohe[:, i]) / X_all_ohe.shape[0]
        if freq > feature_threshold:
            df_cv[new_feature] = X_cv_ohe[:, i]
            df_all[new_feature] = X_all_ohe[:, i]
            feature_names.append(new_feature)
        else:
            low_freq_features.append(i)
    
    # aggregate low frequency features
    if len(low_freq_features) > 0:
        extra_label = col_name + str(X_all_ohe.shape[1])
        feature_names.append(extra_label)
        
        X_all_extra = np.array([0 for x in range(X_all.shape[0])])
        X_cv_extra = np.array([0 for x in range(X_cv.shape[0])])
        
        for i in low_freq_features:
            for idx, val in enumerate(X_all_ohe[:, i]):
                if val == 1:
                    X_all_extra[idx] = 1
            for idx, val in enumerate(X_cv_ohe[:, i]):
                if val == 1:
                    X_cv_extra[idx] = 1
        
        df_cv[extra_label] = X_cv_extra
        df_all[extra_label] = X_all_extra                    
            
    feature_names.remove(col_name)
    df_cv = df_cv.drop(col_name, axis=1)
    df_all = df_all.drop(col_name, axis=1)
    
    return df_cv, df_all, feature_names

