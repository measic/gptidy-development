timings_cuckoo_2 = sorted(timings_cuckoo.items()) #redundant variable, but doing this to make sure this cell can be rerun
timings_bloom_2 = sorted(timings_bloom.items())

load_factors_emp = []
cuckoo_times_array = []
bloom_times_array = []

for key, times in timings_cuckoo_2:
    load_factors_emp.append(key)
    current_y = [np.percentile(times, p) for p in (25, 50, 75)]
    cuckoo_times_array.append(current_y)
    
for key, times in timings_bloom_2:
    current_y = [np.percentile(times, p) for p in (25, 50, 75)]
    bloom_times_array.append(current_y)
    
cuckoo_times_array = np.asarray(cuckoo_times_array)
bloom_times_array = np.asarray(bloom_times_array)