def foldData(data, labels):
    skf = StratifiedKFold(n_splits=10)
    folds = []
    for train_index, dev_index in skf.split(data, labels):
        train_data, dev_data     = data.values[train_index], data.values[dev_index]
        train_labels, dev_labels = labels[train_index], labels[dev_index]        
        folds.append( {'train_data': train_data, 'train_labels': train_labels, 
                        'dev_data':   dev_data,   'dev_labels': dev_labels })
    return folds

