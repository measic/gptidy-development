renamed = datasource.rename(columns={'PC4_LEERL': 'PC4'})
output = pd.merge(renamed, koppeltabel, on='PC4', how='inner')
output.head(10)