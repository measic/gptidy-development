plt.plot(df_per_day.index, df_per_day["client-ip-unique-count"], label='Actuals')
plt.plot(df_per_day.index, df_per_day["client-ip-unique-count-MEAN"], label='MEAN')
plt.legend(loc='best')