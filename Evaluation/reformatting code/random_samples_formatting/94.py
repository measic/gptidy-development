# load the geocoded previous travel history (places visited prior to smartphone/gps)
df_pre = pd.read_csv('data/previous-travels-geocoded.csv', encoding='utf-8')
print('There are {:,} rows in the previous travels data set'.format(len(df_pre)))
df_pre.head()