#create summary table for all region aggregate 
grouped_region_stats = region_stats.groupby(['region']).mean()
region_mean = grouped_region_stats.drop(columns=["school_id"])
region_mean['earnings_cost_ratio'] = region_mean['earnings6years']/region_mean['tuition_in_state']


#drop region 0 and 9
mean_df_clean = region_mean.drop([0,9])
mean_df_clean