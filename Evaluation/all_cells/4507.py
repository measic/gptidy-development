if visualize_dataset == True:
    
    if deal_with_nulls == "remove":
        
        # Print message
        print("Nulls will be removed from visualization dataset.")
        
        # Remove each record containing any nulls
        data_no_nulls = data.dropna(how = "any", axis = 0)

        print("Shape of original dataset {}"\
              .format(data.shape))
        print("Shape of visualization dataset {}. \n{} Records were removed (containing nulls)."\
              .format(data_no_nulls.shape, data.shape[0] - data_no_nulls.shape[0]))
    else:
        # Print message
        
        print("Nulls will be replaced by the mean of each numeric feature.")
        
        # Find each column of numeric quality and store in list
        columns_to_fill_mean = list(
                merged[(merged["data_type"] == "int64") | 
                (merged["data_type"] == "float64")]["index"])
        
        data_no_nulls = data
        
        # For each column in list fill the dataset with the mean of that column
        for column in columns_to_fill_mean:
            data_no_nulls[column] = data_no_nulls[column].fillna(data_no_nulls[column].mean())