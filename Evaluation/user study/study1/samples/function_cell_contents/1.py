def function_def(dbn):
    return dbn[0:2]
combined['school_dist'] = combined['DBN'].apply(function_def)