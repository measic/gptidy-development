t0 = 8000
t1 = 9000
epsilon = 500
ti = t0 - epsilon
tf = t1 + epsilon
tm = ti + (tf - ti) // 2
print(f'ti={ti}, tf={tf}, tm={tm}')