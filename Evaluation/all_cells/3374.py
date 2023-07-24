df_ll = df_vs[['new_lat', 'new_lon']].dropna()
duplicated = df_ll[df_ll.duplicated(keep=False)]
duplicated