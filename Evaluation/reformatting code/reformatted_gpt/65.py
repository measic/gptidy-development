percent_null = percent_null.reset_index().rename(columns={"null_percent"})
percent_filled = percent_filled.reset_index().rename(columns={"non_null_percent"})
filled_count_series = filled_count_series.reset_index().rename(columns={"non_null_counts"})
null_count_series = null_count_series.reset_index().rename(columns={"null_counts"})