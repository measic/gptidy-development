#add Tuition Cost Tier column to dataframe
region_stats["tuition_cost_tier"] = pd.cut(region_stats["tuition_in_state"], bins, labels=bin_names)

#store variables for ratio calculations
cost = region_stats['tuition_in_state']
earnings6 = region_stats['earnings6years']
earnings10 = region_stats['earnings10years']

#add columns for earnings/cost ratio, 6 - 10 year earnings growth ratio
region_stats['earnings_cost_ratio'] = earnings6/cost
region_stats['earnings_growth_y6_y10'] = earnings10/earnings6
region_stats['weighted_growth_to_tuition'] = region_stats['earnings_cost_ratio'] * region_stats['earnings_growth_y6_y10']

