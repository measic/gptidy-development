df_per_day["client-ip-unique-count-log"] = np.log(df_per_day["client-ip-unique-count"])
df_per_day["client-ip-unique-count-log"].hist()