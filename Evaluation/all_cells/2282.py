less = 0
np.bincount(cluster_assignment[10]())
cnt = np.bincount(cluster_assignment[100]())
for i in cnt:
    if i <= 236:
        less += 1
        
print less