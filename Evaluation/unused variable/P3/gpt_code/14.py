def insert_and_time_filter_bloom_filter(capacity, percent_fill=0.9):
    b_filter = CountingBloomFilter(capacity)
    for i in range(int(percent_fill*capacity)):
        b_filter.add(str(i))
    return b_filter