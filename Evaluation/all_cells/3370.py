sub_latlon = df_vs[['new_lat', 'new_lon']].dropna().values
print(f'Out of {len(df_vs)} virtual stations in Hydroweb, {len(sub_latlon)} could be found in HydroSHEDS.')