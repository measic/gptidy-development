import numpy as np

# v1 . v2 = |v1| |v2| cos(a)
# <=> a = cos-1( (v1.v2) / |v1||v2| )

# 5 degrees tolerance is fine!

def debug_vectors(v1, v2):
    print("v1: {0}, v2: {1}".format(v1, v2))
    print("Angle: {0}".format(v_angle(v1, v2)))
    print("Perpendicular: {0}". format(v_perpendicular(v1, v2, 4)))
    print("Parallel: {0}".format(v_parallel(v1, v2, 3)))
    print("Same Orientation: {0}".format(v_same_orientation(v1, v2)))
    print("Dot product: {0}\n".format(np.dot(v1, v2)))

def debug_all_samples(): 
    for sample in samples[0x10] + samples[0x80]:
        va = np.array(sample[1])
        vb = np.array(sample[0])
        o = np.array(sample[3])
        s = np.array(sample[2])

        v1 = (va - o) / np.linalg.norm((va - o))
        v2 = (vb - o) / np.linalg.norm((vb - o))

        debug_vectors(v1, v2)

# vy (1486,68)
# vx (1638,213)
# s  (1581,119)
# o  (1628,69)
        
    
debug_all_samples()


va = np.array([1638, 213]) 
vb = np.array([1486, 68]) 
o = np.array([1628, 69])

real_origin = np.array([0, 0])
translate = real_origin - o

ot = o + translate

vat = (va + translate)
vbt = (vb + translate)

debug_vectors(va - o, vb - o)
debug_vectors(vat, vbt)

print("va: {0}, vb: {1}".format(va,vb))
print("vat: {0}, vbt: {1}".format(vat,vbt))