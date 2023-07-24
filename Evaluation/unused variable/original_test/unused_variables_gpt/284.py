heads_proba = 0.51 # The probability of head is 0.51 as it is a biased coin

# coin_tosses contains the coin tosses for 10 series of 10000 times of coin tosses
coin_tosses = (np.random.rand(10000, 10) < heads_proba).astype(np.int32) 
cumulative_sum_of_number_of_heads = np.cumsum(coin_tosses, axis=0)
cumulative_heads_ratio = cumulative_sum_of_number_of_heads / np.arange(1, 10001).reshape(-1, 1)
cumulative_heads_ratio