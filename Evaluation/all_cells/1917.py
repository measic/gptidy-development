bloom_times = []
cuckoo_times = []

for size in tqdm(capacities):
    
    __, c_time, num_inserted = insert_and_time_filter_cuckoo_filter(int(size))
    cuckoo_times.append(c_time)
    
    __,b_time =  insert_and_time_filter_bloom_filter(num_inserted)
    bloom_times.append(b_time)
