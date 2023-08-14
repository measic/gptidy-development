# cluster parameters
nclusters = 6
dimensions = 2
covariance = [20, 10]
minRange = 0
maxRange = 100
npoints = 100
    
dataset = create_data(nclusters, dimensions, covariance, npoints, minrange=minRange, maxrange=maxRange,
                      random_flip=False, nonlinearities = True)

clusters = np.asarray(data_to_clusters(dataset))

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(8,6)
plot_data(clusters, "", ax, n_clusters=nclusters, minrange=minRange, maxrange=maxRange, covariance=0)
plt.savefig("../Figures/labelled-data.pdf", bbox_inches='tight', pad_inches=0)
plt.show()