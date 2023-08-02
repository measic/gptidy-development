variable_def = pca.inverse_transform(centers)
true_centers = np.exp(variable_def)
segments = ['Segment {}'.format(i) for i in range(0, len(centers))]
true_centers = pd.DataFrame(np.round(true_centers), columns=data.keys())
true_centers.index = segments
display(true_centers)