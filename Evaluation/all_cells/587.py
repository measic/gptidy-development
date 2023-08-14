import numpy as np

# 1 MeV
print "For 1 MeV Mik file:"
bounds = np.linspace(2.0,37,36)   #(First right bin boundary, last right bin, boundary, number of bins)
print len(bounds)
for i in range(0,len(bounds)):
    print '{}                                      right boundary of energy interval {}'.format(bounds[i],i+1)

# 0.5 MeV
print "\nFor 1 MeV Mik file:"
bounds = np.linspace(1.5,37.5,73)   #(First right bin boundary, last right bin, boundary, number of bins)
print len(bounds)
for i in range(0,len(bounds)):
    print '{}                                      right boundary of energy interval {}'.format(bounds[i],i+1)