# round lat-long to 7 decimal points (to prevent fluky floating point .000000000001 stuff) to reduce js data file size
df_combined['lat'] = df_combined['lat'].round(7)
df_combined['lon'] = df_combined['lon'].round(7)