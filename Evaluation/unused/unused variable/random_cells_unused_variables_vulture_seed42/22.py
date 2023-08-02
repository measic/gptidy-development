#Create a monthly mean PM2.5 for the dataset
monthly_data = After2009.resample('M', dim='time', how='mean', keep_attrs=True)