#sanity check
X_frac_arr = []
for j in range(len(mass_frac_ab)):
    X_layer_j = 0
    for i in range(14):
        # check the data
        # print i , 'mass fraction = ', abund_data[0,i+1]
        X_layer_j = X_layer_j + abund_data[j,i+1]
    
        
    X_frac_arr.append(X_layer_j)
        
print 'size of _abund columns: ', len(mass_frac_ab)
max_frac = max(X_frac_arr)
min_frac = min(X_frac_arr)
av_frac = sum(X_frac_arr)/len(mass_frac_ab)
#print abund_data[0,:]
print 'Fraction of shell mass in shell (should = 1) = ', av_frac
print 'Maximum shell fractional mass: shell ', X_frac_arr.index(max_frac), ' with value of ', max_frac
print 'Minimum shell fractional mass: shell ', X_frac_arr.index(min_frac), ' with value of ', min_frac
X_dev_arr = []
for k in X_frac_arr:
    X_dev_arr.append(k - 1)
print X_frac_arr[0], ' - 1 = ',X_dev_arr[0]