import itertools
import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from scipy.spatial import distance

def sample_to_ndarray(sample):
    points = []
    
    for point in sample:
        points.append(point[0])
        points.append(point[1])
    
    return np.array(points)


def render_sample(index):
    df = pd.DataFrame(samples[index], columns=['x', 'y'])
    print(df)
    fig = df.plot.scatter(x='x', y='y', color='red', figsize=(15,15))

    fig.set_xlim([0, 2000])
    fig.set_ylim([0, 2000])

    plt.gca().set_aspect('equal', adjustable='box')
    plt.ylabel('some numbers')

    plt.show()

def convex_hull(sample):
    # convert points of sample to ndarray
    points = np.asarray(sample)
    
    # find the convex hull
    hull = ConvexHull(points)    
   
    plt.figure(num=None, figsize=(18, 16), dpi=320, facecolor='w', edgecolor='r')
    
    plt.xlim([0,2000]) 
    plt.ylim([0,2000]) 

    # plot the original points
    plt.plot(points[:, 0], points[:, 1], 'o')

    # plot the convex hull around it
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'r')

    # adjustment to coordinate system
    plt.gca().set_aspect('equal', adjustable='box')
    
    # display that crap
    plt.show()


def get_distances_for_sample(sample):
    oy = sample[0]
    ox = sample[1]
    tc = sample[2] # part of the code
    origin = sample[3] # origin

    return[distance.euclidean(origin, ox), distance.euclidean(origin, oy),distance.euclidean(ox, oy),distance.euclidean(tc, origin) ]
    

def get_statistics_for_sampleset(sampleset):
    dst_origin_ox = []
    dst_origin_oy = []
    dst_ox_oy = []
    dst_origin_tc = []

    for i in range(0,9): 
        sample = samples[0b10000000][i]
        distances = get_distances_for_sample(sample)
        
        dst_origin_ox.append(distances[0])
        dst_origin_oy.append(distances[1])
        dst_ox_oy.append(distances[2])
        dst_origin_tc.append(distances[3])

    print("dst(origin,x): mean({0}), max({1}, min({2}))".format(np.mean(dst_origin_ox), np.max(dst_origin_ox), np.min(dst_origin_ox)))
    print("dst(origin,y): mean({0}), max({1}, min({2}))".format(np.mean(dst_origin_oy), np.max(dst_origin_oy), np.min(dst_origin_oy)))
    print("dst(ox,oy): mean({0}), max({1}, min({2}))".format(np.mean(dst_ox_oy), np.max(dst_ox_oy), np.min(dst_ox_oy)))
    print("dst(origin,tc): mean({0}), max({1}, min({2}))".format(np.mean(dst_origin_tc), np.max(dst_origin_tc), np.min(dst_origin_tc)))

    
sample = samples[0x10][3]
om = get_orientation_marks(sample)
print(norm(om, sample[2]))

convex_hull(sample)
#get_statistics_for_sampleset(samples[0x80])

