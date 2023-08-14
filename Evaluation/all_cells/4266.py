# Calculate the percentage of each category
samples_w_total = samples.copy()
samples_w_total['Total'] = samples_w_total.sum(axis=1)
samples_percentage = samples.loc[:,"Fresh":"Delicatessen"].div(samples_w_total['Total'], axis=0) * 100
samples_percentage['Total'] = samples_percentage.sum(axis=1)
samples_percentage