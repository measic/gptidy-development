plt.plot(df_per_day.index,df_per_day['client-ip-unique-count'],label="Unique IP")
plt.plot(df_per_day.index,df_per_day['cs-username-unique-count'],label="Unique User")
plt.legend()