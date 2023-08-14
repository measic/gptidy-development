# create variables
df_secs['frac'] = mdl.continuous_var_list(securities, name='frac', ub=1)