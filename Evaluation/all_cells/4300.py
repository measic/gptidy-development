
# TODO: Inverse transform the centers
log_centers = pca.inverse_transform(centers)

# TODO: Exponentiate the centers
true_centers = np.exp(log_centers)

# Display the true centers
segments = ['Segment {}'.format(i) for i in range(0,len(centers))]
true_centers = pd.DataFrame(np.round(true_centers), columns = data.keys())
true_centers.index = segments
print ("True Centers")
display(true_centers)

mean_comparison = true_centers - data.mean().round()
median_comparison = true_centers - data.median().round()
print ("Compared to the mean: ")
display(mean_comparison)
print ("Compared to the median: ")
display(median_comparison)