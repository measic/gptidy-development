def read_s3_csv (dates):
    s3 = boto3.resource('s3')
    deutsche_boerse_bucket = 'deutsche-boerse-xetra-pds'
    
    bucket = s3.Bucket(deutsche_boerse_bucket)
    
    dataframes = []
    
    for date in dates:
        objs_count = 0
        csv_objects = bucket.objects.filter(Prefix=date)
        for csv_obj in csv_objects:
            csv_key = csv_obj.key
            if csv_key[-4:] == '.csv':
                objs_count += 1
                csv_body = csv_obj.get()['Body']
                df = pd.read_csv(csv_body)
                dataframes.append(df)
        
        print ("Loaded {} data objects for {}".format (objs_count, date))
    return pd.concat(dataframes)