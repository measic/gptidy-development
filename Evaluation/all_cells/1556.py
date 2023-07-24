#Sort the data along the time dimension
PM25 = PM25.isel(time=np.argsort(PM25.time))