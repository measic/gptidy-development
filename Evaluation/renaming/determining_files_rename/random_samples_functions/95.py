def function_def(data, k, maxiter, num_runs, seed_list=None, verbose=False):
    heterogeneity = {}
    min_heterogeneity_achieved = float('inf')
    best_seed = None
    final_centroids = None
    final_cluster_assignment = None
    for i in xrange(num_runs):
        if seed_list is not None:
            seed = seed_list[i]
            np.random.seed(seed)
        else:
            seed = int(time.time())
            np.random.seed(seed)
        initial_centroids = get_initial_centroids(data, k, seed=0)
        centroids, cluster_assignment = kmeans(data, k, initial_centroids, maxiter=400, record_heterogeneity=None, verbose=True)
        heterogeneity[seed] = compute_heterogeneity(data, k, centroids, cluster_assignment)
        if verbose:
            print('seed={0:06d}, heterogeneity={1:.5f}'.format(seed, heterogeneity[seed]))
            sys.stdout.flush()
        if heterogeneity[seed] < min_heterogeneity_achieved:
            min_heterogeneity_achieved = heterogeneity[seed]
            best_seed = seed
            final_centroids = centroids
            final_cluster_assignment = cluster_assignment
    return (final_centroids, final_cluster_assignment)