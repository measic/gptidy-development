#test group by region
table10k = df0_10k_grouped.drop(['tuition_in_state','earnings6years',
                                 'earnings10years','earnings_cost_ratio','earnings_growth_y6_y10'], axis = 1)

table10k.rename(columns={'weighted_growth_to_tuition':'Worth-It Ratio'})