#Similarly we can create for loop to calculate the entries of mdat
#some data that corresponds to each cat. e.g. age
data = np.array([4,14,6,11,3,14,8,17,17,12,10,18])
#type of cat (of 3 types)
cat = np.array([1,3,2,1,2,2,3,1,3,2,3,1])
print(data[cat==1])
for i in range(0,3):
    # note the +1 because our indexing is base 0 but the categories are 1,2,3 (no 0)
    mdat[i] = np.mean(data[cat==i+1])
print(mdat)
