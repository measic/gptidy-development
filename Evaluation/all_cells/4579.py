# A nested FOR loop to get all possible combinations
perm = []

for i in ['a', 'b', 'c']:
    for j in ['a', 'b', 'c']:
        perm.append(i+j)
        
print(perm)