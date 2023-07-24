n_core = 2   # Number of cores to be used for the parallel computation
with NoDaemonPool(n_core) as pool:
    for ret in pool.map(return_itself, range(5)):
        print(ret)