# Write a function marginalize that given
def marginalize(P, dim):
    return np.sum(P, axis=tuple(set(range(P.ndim)) - {dim}))
    
    
    
# Lets try it
test_P = np.random.rand(2, 3, 4)
test_P = test_P / test_P.sum()  # Normalize for proper distribution

# Do the marginal distributions look like you expect?
print (marginalize(test_P, 0))
print (marginalize(test_P, 1))
print (marginalize(test_P, 2))
