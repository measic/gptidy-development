import eda
reload(eda)
log_data2 = log_data.loc[[x for x in log_data.index if x not in d_unique_idx.keys()]]
variable_def = log_data.loc[[x[0] for x in d_unique_idx.iteritems() if x[1] > 1]]
ax = eda.features_boxplot(log_data2, variable_def, variable_def.index)