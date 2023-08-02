samples_w_total = samples.copy()
samples_w_total['Total'] = samples_w_total.sum(axis=1)
variable_def = samples.loc[:, 'Fresh':'Delicatessen'].div(samples_w_total['Total'], axis=0) * 100
variable_def['Total'] = variable_def.sum(axis=1)
variable_def