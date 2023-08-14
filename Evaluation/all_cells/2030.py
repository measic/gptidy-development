log_and_placements_aggregated_per_week_df["client-ip-unique-count-MEAN"] =log_and_placements_aggregated_per_week_df["client-ip-unique-count"].mean()


log_and_placements_aggregated_per_week_df["AE"]=np.abs(
    log_and_placements_aggregated_per_week_df["client-ip-unique-count"]- 
    log_and_placements_aggregated_per_week_df["client-ip-unique-count-MEAN"]
)

log_and_placements_aggregated_per_week_df.AE.mean()