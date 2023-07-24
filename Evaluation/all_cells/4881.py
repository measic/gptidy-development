# For each feature find the data points with extreme high or low values
d_unique_idx = dict()
print "Number of Data points considered outliers for the feature\n"
for feature in log_data.keys():
    
    # TODO: Calculate Q1 (25th percentile of the data) for the given feature
    Q1 = np.percentile(log_data[feature], 25)
    
    # TODO: Calculate Q3 (75th percentile of the data) for the given feature
    Q3 = np.percentile(log_data[feature], 75)
    
    # TODO: Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
    step = 1.5*(Q3-Q1)
    
    # Display the outliers
    df_out_lier = log_data[~((log_data[feature] >= Q1 - step) & (log_data[feature] <= Q3 + step))]
    i_nfeatures = df_out_lier.shape[0]
    print "{:18s}\t{:18s}".format(feature, str(i_nfeatures))
    for x in df_out_lier.index:
        if x not in d_unique_idx.keys():
            d_unique_idx[x] = 1
        else:
            d_unique_idx[x] += 1

print "-------------------------"
print "TOTAL: Outliers: {} | Unique Outliers: {}".format(sum(d_unique_idx.values()),
                                                         len(d_unique_idx.keys()))
# filtering just the repeated outliers
print "\n\nData points considered outliers for more than one feature:"
df_aux = log_data.loc[[x[0] for x in d_unique_idx.iteritems() if x[1]>1]]
df_aux['count'] = None
df_aux['count'] = [d_unique_idx[x] for x in df_aux.index]
df_aux