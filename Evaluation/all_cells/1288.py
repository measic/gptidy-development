#organize seperate dataframes by cost tier for plotting + drop region 0 & 9 due to irrelevancy 
df0_10k = clean_info.loc[clean_info["tuition_cost_tier"] == 'less_10k']
df0_10k_edit0 = df0_10k[df0_10k.region != 0]
df0_10k_edit9 = df0_10k_edit0[df0_10k_edit0.region != 9]

df10_18k = clean_info.loc[clean_info["tuition_cost_tier"] == '10k_18k']
df10_18k_edit = df10_18k[df10_18k.region != 9]

df18_32 = clean_info.loc[clean_info["tuition_cost_tier"] == '18k_32k']

df32 = clean_info.loc[clean_info["tuition_cost_tier"] == 'greater_32k']