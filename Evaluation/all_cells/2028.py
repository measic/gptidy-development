sns.pairplot(data=log_and_placements_aggregated_per_week_df
             ,vars=['client-ip-unique-count-log','client-ip-unique-count-log','cs-username-unique-count',
                    'PlacementCount', 'PlacementCompletedCount',
                    'PlacementAllocatedInProgressCount'])