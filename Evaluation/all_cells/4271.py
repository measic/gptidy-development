# For each feature find the data points with extreme high or low values

all_outliers = []

for feature in log_data.keys():
    
    # TODO: Calculate Q1 (25th percentile of the data) for the given feature
    Q1 = np.percentile(log_data[feature], 25)
    
    # TODO: Calculate Q3 (75th percentile of the data) for the given feature
    Q3 = np.percentile(log_data[feature], 75)
    
    # TODO: Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
    step = (Q3 - Q1) * 1.5
    
    # Display the outliers
    print "Data points considered outliers for the feature '{}':".format(feature)
    df_outliers = log_data[~((log_data[feature] >= Q1 - step) & (log_data[feature] <= Q3 + step))]
    display(df_outliers)
    
    # Append outliers to list
    all_outliers += list(df_outliers.index.values)

    
# ALL UNIQUE OUTLIERS, INCLUIDING THOSE REPEATED BETWEEN CATEGORIES
print "\nAll unique outliers (including repeated between categories):"
unique_outliers = list(set(all_outliers))
print unique_outliers

# ONLY OUTLIERS FOUND IN MORE THAN ONE CATEGORY
outliers_more_than_1_cat = list(set([x for x in all_outliers if all_outliers.count(x) > 1]))
print "\nOutliers found in more than ONE category:"
print outliers_more_than_1_cat

# ALL OUTLIERS EXCEPT THE ONES FOUND IN MORE THAN ONE CATEGORY
outliers_in_exactly_1_cat = list(set([x for x in all_outliers if all_outliers.count(x) == 1]))
print "\nOutliers that are NOT found in more than ONE category:"
print outliers_in_exactly_1_cat
    
# OPTIONAL: Select the indices for data points you wish to remove
outliers  = unique_outliers

# Remove the outliers, if any were specified
good_data = log_data.drop(log_data.index[outliers]).reset_index(drop = True)