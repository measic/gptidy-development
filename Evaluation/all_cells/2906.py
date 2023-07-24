df_fsq = pd.read_csv('data/foursquare-location-history.csv', encoding='utf-8')
print('There are {:,} rows in the foursquare data set'.format(len(df_fsq)))
df_fsq.head()