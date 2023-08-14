#Select monthly mean PM2.5 data for the LSOA
ts = monthly_data.isel(x=1103, y=1045).load()