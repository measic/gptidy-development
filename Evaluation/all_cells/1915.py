def insert_and_time_filter_cuckoo_filter(capacity, percent_fill=0.9):
    num_inserted = 0
    c_filter = CuckooFilter(capacity, 2)
    now = time.time()
    for i in range(int(percent_fill*capacity)):
        try:
            c_filter.insert(str(i))
            num_inserted += 1
        except Exception("CuckooFilter has filled up!"):
            break
    elapsed_insertion = time.time() - now
    return c_filter, elapsed_insertion, num_inserted