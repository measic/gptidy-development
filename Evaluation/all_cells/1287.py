#drop uneccesary columns for analysis
clean_info = region_stats.drop(columns=['school_id', 'tuition_out_state'])
