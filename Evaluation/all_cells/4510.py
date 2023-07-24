data_no_nulls_column_list = list(data_no_nulls.columns)

if visualize_dataset == True:
    for feature in features_to_exclude:
        if feature in data_no_nulls_column_list:
            data_no_nulls.drop([feature], axis = 1, inplace = True)
            print("{} removed from visualization dataset".format(feature))