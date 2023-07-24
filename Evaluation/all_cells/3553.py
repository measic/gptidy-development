subset_uuid = ekos.get_unique_id_for_alias(workspace_alias = workspace_alias, subset_alias = 'A')
print(w.get_subset_list(), subset_uuid)

f1 = w.get_data_filter_object(subset = subset_uuid, step=1) 
print(f1.include_list_filter)

w.apply_data_filter(subset = subset_uuid, step = 1)

df_step1 = w.get_filtered_data(step = 1, subset = subset_uuid)
#print(df_step1.columns)
#df_step1[['SDATE', 'YEAR', 'MONTH', 'POSITION', 'VISS_EU_CD', 'WATER_TYPE_AREA', 'DEPH', 'MNDEP', 'MXDEP','BQIm']].dropna(subset = ['BQIm'])