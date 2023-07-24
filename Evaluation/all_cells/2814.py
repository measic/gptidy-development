# Now let's log-transform the skewed features
for col in skewed_features:
   data_full[col] = np.log1p(data_full[col])