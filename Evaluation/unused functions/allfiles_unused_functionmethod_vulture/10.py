def engineer_date_range (dates):
    unprocessed_df = read_s3_csv (dates)
    print ("Loaded CSV data set from S3")
    
    cleaned_df = clean_data (unprocessed_df, inplace = True)
    print ("Cleaned CSV data set")
     
    xgb_data = create_xgb_features (cleaned_df, 5, inplace=True)
    xgb_data['NextMaxPrice'] = create_xgb_target (xgb_data)
    print ("Engineered CSV data set")
    
    train_data, validate_data = train_test_split (xgb_data, train_size=0.8, test_size=0.2, shuffle=True)

    cols = list(train_data.columns.values)
    cols.remove ('NextMaxPrice')
    cols = ['NextMaxPrice'] + cols

    train_data = pd.get_dummies (train_data[cols])
    validate_data = pd.get_dummies (validate_data[cols])
    print ("Data split for training purposes")
    
    return (train_data, validate_data)