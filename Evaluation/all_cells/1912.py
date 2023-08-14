load_factors_of_interest = np.linspace(0.1, 0.8, 8)
capacity = 3e4
num_items_to_insert = 500
num_runs = 30
timings_cuckoo = defaultdict(list)
timings_bloom = defaultdict(list)

for load in tqdm(load_factors_of_interest, "current run"):
    for run in tqdm(range(num_runs)):
        c_filt, _ = return_cuckoo_filter_with_specified_load_factor(int(capacity),\
                                                                                 finger_print_size=2, load_factor=load)
        b_filt, _ = return_bloom_filter_with_specified_load_factor(int(capacity), percent_to_fill=load)
        
        start = time.time()
        for item_to_insert in range(num_items_to_insert):
            item = "".join(random.sample(string.ascii_lowercase, 12))
            c_filt.add(item)
        dt_cuckoo = time.time() - start
        timings_cuckoo[load].append(dt_cuckoo)
        
        start = time.time()
        for item_to_insert in range(num_items_to_insert):
            item = "".join(random.sample(string.ascii_lowercase, 12))
            b_filt.add(item)
        dt_bloom = time.time() - start
        timings_bloom[load].append(dt_bloom)