def counting_bloom_and_cuckoo_filter_fpr(capacity, finger_print_size=0.5, bucket_size=4,\
                                         number_of_bytes=100000, alpha=0.75):
    alpha = number_of_bytes / (capacity * finger_print_size * bucket_size)
    
    analytic_bloom_error = exp(-(((number_of_bytes-1)*log(2)**2)/capacity) ) 
    
    analytic_cuckoo_error = 1 / (2**( finger_print_size*alpha*8 - log(2*bucket_size, 2)))#this is estimated from the paper
     
    return analytic_bloom_error, analytic_cuckoo_error