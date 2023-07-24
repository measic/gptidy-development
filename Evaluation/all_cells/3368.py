cluster = Cluster(n_workers=n_workers)
client = Client(cluster)
cluster