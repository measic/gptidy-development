df_per_day_train = df_per_day.loc[:299,['client-ip-unique-count-log']]
df_per_day_test= df_per_day.loc[300:,['client-ip-unique-count-log']]