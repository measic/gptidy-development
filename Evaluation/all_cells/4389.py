prob = 0
from decimal import Decimal
n = 2000
for i in range(1, n//2):
    prob += np.multiply(np.multiply(nCr(n, i), Decimal(0.51 ** (n-i))), Decimal(0.49 ** i))
    
prob 
