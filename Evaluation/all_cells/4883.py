# OPTIONAL: Select the indices for data points you wish to remove
outliers  = [154, 128, 75, 66]

# Remove the outliers, if any were specified
good_data = log_data.drop(log_data.index[outliers]).reset_index(drop = True)