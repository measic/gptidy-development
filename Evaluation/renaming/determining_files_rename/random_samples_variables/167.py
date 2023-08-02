variable_def = samples.copy()
variable_def['Total'] = variable_def.sum(axis=1)
samples_percentage = samples.loc[:, 'Fresh':'Delicatessen'].div(variable_def['Total'], axis=0) * 100
samples_percentage['Total'] = samples_percentage.sum(axis=1)
samples_percentage