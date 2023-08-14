bloom_times_deletion = []
cuckoo_times_deletion = []

for size in tqdm(capacities):
    __,b_time =  delete_from_bloom_filter_and_time(int(size), percent_to_fill=0.9, percent_delete=1.0)
    bloom_times_deletion.append(b_time)
    
    __, c_time = delete_from_cuckoo_filter_and_time(int(size), percent_to_fill=0.9, percent_delete=1.0)
    cuckoo_times_deletion.append(c_time)