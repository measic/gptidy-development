def get_data_from_tsv(feature_file, x_fields, y_field, x_filter=None, seed=0, as_np_array=False, scale=False, shuffle=False, train_portion=0.6, test_portion=0.2):
    my_data = pandas.read_csv(feature_file)
    print(my_data.shape)
    my_data = my_data.dropna()
    my_data = my_data.reset_index(drop=True)
    print(my_data.shape)
    if not x_filter == None:
        for ff in x_filter:
            my_data = my_data[my_data[ff[0]].isin(ff[1:])]
            print('filtering %s by ' % ff[0], ff[1:], 'num datapoints left: ', len(my_data))
        my_data = my_data.reset_index(drop=True)
    labels = my_data['word']
    if 'freq' in x_fields or my_data.columns.get_loc('freq') in x_fields:
        idx = my_data.columns.get_loc('freq')
        my_data.iloc[:, idx] = np.log(my_data.iloc[:, idx])
        my_data = my_data.rename(columns={'freq': 'log_freq'})
    if 'length' in x_fields or my_data.columns.get_loc('length') in x_fields:
        idx = my_data.columns.get_loc('length')
        my_data.iloc[:, idx] = np.log(my_data.iloc[:, idx])
        my_data = my_data.rename(columns={'length': 'log_length'})
    if type(x_fields[0]) == str:
        x_fields.append(y_field)
        my_data = my_data[x_fields]
    else:
        x_fields.append(my_data.columns.get_loc(y_field))
        my_data = my_data.iloc[:, x_fields]
    del x_fields[-1]
    x_train, y_train, x_dev, y_dev, x_test, variable_def = train_validate_test_split(my_data, y_field, train_percent=train_portion, validate_percent=test_portion, seed=seed, shuffle=shuffle)
    if scale:
        x_train = pandas.DataFrame(preprocessing.scale(x_train), columns=x_train.columns, index=x_train.index)
        x_dev = pandas.DataFrame(preprocessing.scale(x_dev), columns=x_dev.columns, index=x_dev.index)
        x_test = pandas.DataFrame(preprocessing.scale(x_test), columns=x_test.columns, index=x_test.index)
        y_train = pandas.DataFrame(preprocessing.scale(y_train), columns=y_train.columns, index=y_train.index)
        y_dev = pandas.DataFrame(preprocessing.scale(y_dev), columns=y_dev.columns, index=y_dev.index)
        variable_def = pandas.DataFrame(preprocessing.scale(variable_def), columns=variable_def.columns, index=variable_def.index)
    if as_np_array:
        x_train = np.array(x_train).astype(np.float)
        y_train = np.array(y_train).astype(np.float)
        x_dev = np.array(x_dev).astype(np.float)
        y_dev = np.array(y_dev).astype(np.float)
        x_test = np.array(x_test).astype(np.float)
        variable_def = np.array(variable_def).astype(np.float)
    return (x_train, y_train, x_dev, y_dev, x_test, variable_def, labels)