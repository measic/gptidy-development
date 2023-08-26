def sframe_to_scipy(x, column_name):
    """
    Convert a dictionary column of an SFrame into a sparse matrix format where
    each (row_id, column_id, value) triple corresponds to the value of
    x[row_id][column_id], where column_id is a key in the dictionary.
       
    Example
    >>> sparse_matrix, map_key_to_index = sframe_to_scipy(sframe, column_name)
    """
    assert x[column_name].dtype() == dict, 'The chosen column must be dict type, representing sparse data.'
    x = x.add_row_number()
    x = x.stack(column_name, ['feature', 'value'])
    f = graphlab.feature_engineering.OneHotEncoder(features=['feature'])
    f.fit(x)
    x = f.transform(x)
    mapping = f['feature_encoding']
    x['feature_id'] = x['encoded_features'].dict_keys().apply(lambda x: x[0])
    i = np.array(x['id'])
    j = np.array(x['feature_id'])
    v = np.array(x['value'])
    width = x['id'].max() + 1
    height = x['feature_id'].max() + 1
    variable_def = csr_matrix((v, (i, j)), shape=(width, height))
    return (variable_def, mapping)