call = BlackScholes('call', 100., 100., .5, 0.01, 0., .35)
print '-' * 85
print 'BS Price:', call.value, 'BS Delta:', call.delta
print '-' * 85
scenarios = {'1': [1e4, 1e7], 
             '2': [1e4, 1e7], 
             '3': [1e4, 1e7],
             '4': [1e4, 1e7],
             '5': [1e4, 1e7],
             '6': [1e4, 1e7]}
results = {}
for num_processes in scenarios:
    for N in scenarios[num_processes]:
        start = time.time()
        chunks = [int(ceil(N / int(num_processes)))] * int(num_processes)
        chunks[-1] = int(chunks[-1] - sum(chunks) + N)
        p = multiprocessing.Pool(int(num_processes))
        option_value = p.map(value_in_pool, chunks)
        p.close()
        p.join()
        q = multiprocessing.Pool(int(num_processes))
        option_delta = q.map(delta_in_pool, chunks)
        q.close()
        q.join()
        end = time.time()
        print 'Number of processors:', num_processes + ',',
        print 'Number of simulations:', str(int(N))
        print 'Monte Carlo Option Price:', str(mean(option_value)) + ',',
        print 'Monte Carlo Option Delta:', str(mean(option_delta))
        print 'Time, in sec:', str(end - start)
        print '-' * 85
        if N == 1e7: results[num_processes] = (end - start) 
