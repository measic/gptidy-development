#!/usr/bin/env python
# this script plots the mean of data for each category
import numpy as np
import matplotlib.pyplot as plt
data=np.array([4, 14, 6, 11, 3, 14, 8, 17, 17, 12, 10, 18])
cat = np.array([1, 3, 2, 1, 2, 2, 3, 1, 3, 2, 3, 1])
#must initialize the array
mdat = np.zeros(3)
print(mdat)
mdat[0] = np.mean(data[cat==1])
mdat[1] = np.mean(data[cat==2])
mdat[2] = np.mean(data[cat==3])
print(mdat)
x = range(0,3)
plt.plot(x, mdat,'r-*')
plt.title('Mean of data for each category')
plt.savefig('Figure-script.png')  
