capacities = [1e3, 3e3, 1e4, 3e4, 1e5, 3e5, 1e6, 3e6]
bloom_fp = []
cuckoo_fp = []

for size in capacities:
    bfp, cfp = counting_bloom_and_cuckoo_filter_fpr(size, finger_print_size=0.5, bucket_size=4, alpha=0.8)
    bloom_fp.append(bfp)
    cuckoo_fp.append(cfp)