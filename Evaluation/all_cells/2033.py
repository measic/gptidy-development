plt.plot(log_and_placements_aggregated_per_week_df.index, log_and_placements_aggregated_per_week_df["client-ip-unique-count"], label='Actuals')
plt.plot(log_and_placements_aggregated_per_week_df.index, log_and_placements_aggregated_per_week_df["client-ip-unique-count-MEAN"], label='MEAN')
plt.legend(loc='best')