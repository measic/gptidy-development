for model in ['ridge', 'lasso', 'elastic']:
    filebasename = 'kaggle_export'
    timestamp = datetime.today().strftime('%Y%m%d-%H%M%S')
    filename = filebasename + timestamp + model
    table = make_export_table(model)
    table.to_csv(filename, index = False)