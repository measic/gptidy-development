def return_cuckoo_filter_with_specified_load_factor(capacity, finger_print_size=2, load_factor=0.2):
    c_filter = CuckooFilter(capacity, finger_print_size, bucket_size=2)
    for i in range(int(capacity*6)):
        try:
            item = "".join(random.sample(string.ascii_lowercase, 12))
            c_filter.add(item)
        except Exception('CuckooFilter has filled up!'):
            break
            
        if round(c_filter.get_load_factor(), 2) == round(load_factor, 2):
            return c_filter, c_filter.get_load_factor()
    raise ValueError

def return_bloom_filter_with_specified_load_factor(capacity, percent_to_fill=0.2):
    b_filter = CountingBloomFilter(capacity)
    for i in range(int(percent_to_fill*capacity)):
        item = "".join(random.sample(string.ascii_lowercase, 12))
        b_filter.add(item)
    
    return b_filter, percent_to_fill