def splitData(data, labels):
    train_data_all, test_data, train_labels_all, test_labels = train_test_split(data, labels,
                                                               stratify=labels, 
                                                               test_size=0.25)

    train_data, dev_data, train_labels, dev_labels = train_test_split(train_data_all, train_labels_all,
                                                                     stratify=train_labels_all, 
                                                                     test_size=0.20)

    print("training data:", train_data.shape)
    print("dev data     :", dev_data.shape)
    print("test data    :",  test_data.shape)
    return {'train_data': train_data, 'train_labels': train_labels, 
            'dev_data':   dev_data,   'dev_labels': dev_labels,
            'test_data':  test_data,  'test_labels': test_labels}

